#
# Author: Richard Penman
# License: LGPL
# Description: 
# Model the desired information in a webpage.
#

from __future__ import nested_scopes, generators, division, absolute_import, with_statement
import sys
import os
import re
import string
import urllib2
from difflib import SequenceMatcher
from . import misc
from lxml import etree, html

UNDEFINED = -1



class xmlAttributes(object):
    """Extract attributes from XML tree and store them reverse indexed by attribute

    >>> X1 = xmlXpaths('file:data/html/search/yahoo/1.html')
    >>> X2 = xmlXpaths('file:data/html/search/yahoo/2.html')
    >>> X3 = xmlXpaths('file:data/html/search/yahoo/3.html')
    >>> a = xmlAttributes([X1, X2, X2])
    >>> a.breakXpath('/a/b/c')
    ['/a', '/a/b', '/a/b/c']
    >>> xpath = '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/span[1]'
    >>> e1 = X1.getTree().xpath(xpath)[0]
    >>> e2 = X1.getTree().xpath(xpath)[0]
    >>> a.extractAttribs(e1)
    [('class', 'url')]
    >>> attribs = a.uniqueAttribs(xpath)
    >>> attribs
    [[], [('lang', 'en')], [('id', 'ysch')], [('id', 'doc')], [('id', 'bd')], [('id', 'results')], [('id', 'left')], [('id', 'main')], [('id', 'web')], [('start', '1')], [], [('class', 'res')], [('class', 'url')]]
    >>> a.addAttribs(xpath, attribs)
    "/html[@lang='en']/body[@id='ysch']/div[@id='doc']/div[@id='bd']/div[@id='results']/div[@id='left']/div[@id='main']/div[@id='web']/ol[@start='1']/li/div[@class='res']/span[@class='url']"

    >> tree = html.fromstring("<html><body node='0'><c class='1' node='1'>C<d class='2'></d></c><c class='1' node='2'>D</c></body</html>").getroottree()
    >> a = xmlAttributes(tree)
    >> extractXpaths(tree)
    {'C': ['/html[1]/body[1]/c[1]'], 'D': ['/html[1]/body[1]/c[2]']}
    >> a.extractAttribs(['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]'])
    {('node', '0'): ['/html[1]/body[1]'], ('node', '2'): ['/html[1]/body[1]/c[2]'], ('node', '1'): ['/html[1]/body[1]/c[1]'], ('class', '1'): ['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]']}
    >> attribs = a.commonAttribs(['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]'])
    >> attribs
    [('/html[1]/body[1]', ('node', '0')), ('/html[1]/body[1]/c[2]', ('class', '1'))]
    >> a.addCommonAttribs(attribs, ['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]'])
    ["/html[1]/body[1][@node='0']/c[1][@class='1']", "/html[1]/body[1][@node='0']/c[2][@class='1']"]
    """


    def __init__(self, Xs):
        self.Xs = Xs


    def uniqueAttribs(self, xpath):
        """Return a list of attributes that uniquely distinguish the element at each segment"""
        acceptedAttribs = [[]]
        # select examples which contain the relevant xpath
        Xs = [X for X in self.Xs if X.getTree().xpath(xpath)]
        for section in self.breakXpath(xpath):
            sectionElements = misc.flatten([X.getTree().xpath(section) for X in Xs])
            proposedAttribs = self.commonAttribs(sectionElements)
            """if len(sectionElements) == len(Xs):
                # expect a single result, so add index
                index = 0
                for e in sectionElements:
                    index += 1
                    while 1:
                        e = e.getprevious()
                        if e:
                            print proposedAttribs, e.attrib.items()
                            if misc.allIn(proposedAttribs, e.attrib.items()):
                                index += 1
                        else:
                            break
                sectionXpath = self.addAttribs(section, section.count('/')*[[]] + [proposedAttribs])
                print int(round(index // len(Xs))), sectionXpath, [X.getTree().xpath(sectionXpath) for X in Xs]
                #proposedAttribs.append(index)"""
            acceptedAttribs.append(proposedAttribs)
        return acceptedAttribs


    def breakXpath(self, xpath):
        """Break xpath into sections so can match attributes over all parts"""
        xpaths = []
        sections = xpath.split('/')
        for i in range(1, len(sections)):
            xpaths.append('/'.join(sections[:i+1]))
        return xpaths


    def extractAttribs(self, element):
        """Return a list of attributes for the element"""
        attribs = []
        for attrib in element.attrib.items():
            attrName, attrValue = attrib
            if not misc.anyIn(string.punctuation, attrValue+attrName):# and attrName in ('id'):
                attribs.append(attrib)
        return attribs


    def commonAttribs(self, elements):
        """Return a list of common attributes among a group of elements"""
        common = {}
        for e in elements:
            for attrib in self.extractAttribs(e):
                common.setdefault(attrib, 0)
                common[attrib] += 1
        minCount = len(elements)# // 2 + 1
        return [attrib for (attrib, count) in common.items() if count >= minCount]


    def addUniqueAttribs(self, xpath):
        return self.addAttribs(xpath, self.uniqueAttribs(xpath))


    def addAttribs(self, xpath, attribsList):
        """Add attributes to xpath"""
        sections = []
        for section, attribs in zip(xpath.split('/'), attribsList):
            if attribs:
                section = re.sub('\[\d+\]', '', section)
            for attrib in attribs:
                if type(attrib) == int:
                    section += '[%d]' % attrib
                else:
                    section += "[@%s='%s']" % attrib
            sections.append(section)
        return '/'.join(sections)



class xmlXpaths(object):
    """Encapsulates the Xpaths of an XML document
    >>> X = xmlXpaths('file:data/html/search/yahoo/1.html')
    >>> X.normalizeXpath('/html/body/div/table[2]/tr/td/div[2]/*/div')
    '/html[1]/body[1]/div[1]/table[2]/tr[1]/td[1]/div[2]/*/div[1]'
    >>> len(X.extractXpaths())
    325
    >>> xpath = '/html/body/div/div[2]/div[2]/div[2]/div/div[3]/ol[1]/li/div[1]/span[1]'
    >>> xpath = X.normalizeXpath(xpath)
    >>> xpath
    '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/span[1]'
    >>> e = X.getTree().xpath(xpath)[0]
    >>> X.getElementText(e)
    'www.shopzilla.com/10J--Digital_Cameras_-_cat_id--402'
    >>> X.matchXpaths("Bargain prices on Digital Cameras, store variety for Digital Cameras. Compare prices and buy online at Shopzilla.")
    ['/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[2]']
    >>> xmlXpaths.reduceXpaths(['/html[1]/table[1]/tr[1]/td[1]', '/html[1]/table[1]/tr[2]/td[1]', '/html[1]/table[1]/tr[3]/td[1]', '/html[1]/body[1]/a[1]'], [X])
    ['/html[1]/body[1]/a[1]', '/html[1]/table[1]/tr/td[1]']
    """

    # ignore content from these tags
    IGNORE_TAGS = 'style', 'script', 'meta', 'link'
    # merge these style tags content with parent
    MERGE_TAGS = 'br', 'font', 'a', 'b', 'i', 'em', 'u', 's', 'strong', 'big', 'small', 'tt', 'p'
    # user agent to use in fetching webpages
    USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a9pre) Gecko/2007100205 Minefield/3.0a9pre'


    def __init__(self, url, tree=False, xpaths=False):
        self.setUrl(url)
        if not tree:
            tree = self.parseUrl()
        self.setTree(tree)
        if not xpaths:
            xpaths = self.extractXpaths()
        self.setXpaths(xpaths)


    def getUrl(self):
        return self._url
    def setUrl(self, url):
        self._url = url
    def getTree(self):
        return self._tree
    def setTree(self, tree):
        self._tree = tree
    def getXpaths(self):
        return self._xpaths
    def setXpaths(self, xpaths):
        self._xpaths = xpaths


    def parseUrl(self):
        """Fetch url and return an ElementTree of the parsed XML"""
        fp = urllib2.urlopen(urllib2.Request(self.getUrl(), None, {'User-agent': xmlXpaths.USER_AGENT}))
        tree = html.parse(fp)
        # remove tags that are not useful
        for tag in xmlXpaths.IGNORE_TAGS:
            for item in tree.findall('.//' + tag):
                item.drop_tree()
        return tree


    def extractXpaths(self, element = {}, xpaths = {}):
        """Return a hashtable of the xpath to each text element"""
        try:
            tag = element.tag
        except AttributeError:
            self.extractXpaths(self.getTree().getroot(), xpaths)
        else:
            if type(tag) == type(str()):
                text = self.getElementText(element)
                if text:
                    xpaths.setdefault(text, [])
                    xpath = self.normalizeXpath(self.getTree().getpath(element))
                    if xpath not in xpaths[text]:
                        xpaths[text].append(xpath)
                for child in element:
                    self.extractXpaths(child, xpaths)
        return xpaths


    def getElementText(self, e):
        """Extract text from HtmlElement"""
        text = []
        if e.text:
            text.append(e.text)
        for child in e:
            if child.tag in xmlXpaths.MERGE_TAGS:
                text.append(child.text_content())
            if child.tail:
                text.append(child.tail)
        return misc.normalizeStr(''.join(text).strip())


    # XXX refactor xpath functions into class xmlXpath
    def normalizeXpath(self, xpath):
        """ElementTree can get confused when there is no explicit index, so add where missing"""
        newXpath = []
        for tag in xpath.split('/'):
            newXpath.append(tag)
            if tag and tag != '*' and not tag.endswith(']'):
                newXpath[-1] += '[1]'
        return '/'.join(newXpath)


    def matchXpaths(self, output):
        """Return Find matching xpaths of output and return the top ranked with the size of match""" 
        xpaths = self.getXpaths()
        if output in xpaths:
            # exact match so can return xpaths directly with a perfect match
            return [(xpath, len(output)*len(output)) for xpath in xpaths[output]]
        else:
            # no exact match so return xpaths with Longest Common Sequence (LCS) 3 STDs over the mean
            sequences = []
            s = SequenceMatcher()
            s.set_seq2(misc.normalizeStr(output))
            for text, xpath in xpaths.items():
                s.set_seq1(text)
                # square the length to bias towards longer phrases
                sequences.append((sum(n*n for (i, j, n) in s.get_matching_blocks()), xpath))
            #lens = [l for (l, xpath) in LCSs]
            #minLen = numpy.mean(lens) + 3*numpy.std(lens)
            bestXpaths = misc.flatten([[(xpath, l) for xpath in xpaths] for (l, xpaths) in sequences if l > 0])
            """LCSs = []
            if 'PREMIER John Brumby haz' in output:
                print output
                print minLen
                for text, xpath in xpaths.items():
                    s.set_seq1(text)
                    LCSs.append((sum(n*n for (i, j, n) in s.get_matching_blocks()), str(s.get_matching_blocks()), xpath, text))
                for l, m, xpath, text in sorted(LCSs, reverse=True)[:10]:
                    print '(%d - %s) %s: %s' % (l, m, xpath[0], text)
                    print
                sys.exit()"""
            """for i, xpath in enumerate(bestXpaths):#XXX
                e = self.tree.xpath(xpath)[0]
                text = getElementText(e)
                alltext = misc.normalizeStr(e.text_content())
                s.set_seq1(text)
                textLCS = sum(n for (i, j, n) in s.get_matching_blocks())
                s.set_seq1(alltext)
                alltextLCS = sum(n for (i, j, n) in s.get_matching_blocks())
                #print len(text), textLCS, len(alltext), alltextLCS, len(misc.normalizeStr(output))"""
            return bestXpaths


    def abstractXpaths(xpaths, Xs):
        """Reduce list of xpaths by combining related ones in regular expressions"""
        proposedRegs = {}
        for x1 in xpaths:
            x1tokens = x1.split('/')
            for x2 in xpaths:
                if x1 != x2:
                    x2tokens = x2.split('/')
                    diff = misc.difference(x1tokens, x2tokens)
                    if len(diff) == 1:
                        partition = diff[0]
                        reg = '/'.join(x1tokens[:partition] + ['*'] + x1tokens[partition+1:])
                        proposedRegs.setdefault((reg, partition), 0)
                        proposedRegs[(reg, partition)] += 1

        # proposedRegs now holds the number of matching xpaths for each regular expression
        #   so sort by this amount to favour more useful regular expressions.
        # This is important when extracting 2 columns of data from a webpage where the rows will also match
        acceptedRegs = []
        for reg, partition in misc.sortDict(proposedRegs, True):
            matchedXpaths = []
            matchedTags = []
            regTokens = reg.split('/')
            for xpath in xpaths:
                xpathTokens = xpath.split('/')
                diff = misc.difference(regTokens, xpathTokens)
                if len(diff) == 1:
                    matchedXpaths.append(xpath)
                    matchedTags.append(xpathTokens[diff[0]])
            if not matchedXpaths: 
                continue # these xpaths have already been used by a previous regular expression
            matchedTagIds = sorted(misc.extractInt(tag) for tag in matchedTags)
            minPosition = matchedTagIds[0]

            # apply this regular expression if the content is ordered
            expandReg = matchedTagIds == range(minPosition, len(matchedTagIds)+1)
            if not expandReg:
                # of if there are a different number of child elements on each tree at this location
                expandReg = len(misc.unique(len(X.getTree().xpath(reg)) for X in Xs)) > 1
            if expandReg:
                # use a specific tag if all match, instead of the general '*'
                uniqueTags = misc.unique(tag[:tag.index('[')] for tag in matchedTags)
                if len(uniqueTags) > 1:
                    commonTag = '*'
                else:
                    commonTag = uniqueTags[0]
                # restrict xpath regular expressions to lowest index encountered
                if minPosition > 1:
                    commonTag += '[position()>%d]' % (minPosition - 1)
                #partition = notNormalized(reg)[0]
                reg = '/'.join(regTokens[:partition] + [commonTag] + regTokens[partition+1:])
                # remove this xpaths now so they can't be used by another regular expression
                for xpath in matchedXpaths:
                    xpaths.remove(xpath)
                acceptedRegs.append(reg)
        return xpaths + acceptedRegs
    abstractXpaths = staticmethod(abstractXpaths)



def trainModel(urlOutputs):
    """Train the model using the known output for the given urls"""
    # store relevant xpaths for each output
    allOutputXpaths = []
    Xs = [xmlXpaths(url) for (url, outputs) in urlOutputs]
    for X, (url, outputs) in zip(Xs, urlOutputs):
        for i, output in enumerate(outputs):
            if i == len(allOutputXpaths): allOutputXpaths.append({})
            for xpath, score in X.matchXpaths(output):
                allOutputXpaths[i].setdefault(xpath, 0)
                allOutputXpaths[i][xpath] += score

    # return most frequent xpath for each type
    bestXpaths = []
    for outputXpaths in allOutputXpaths:
        bestXpath = sorted((count, len(xpath), xpath) for (xpath, count) in outputXpaths.items())[-1][-1]
        if bestXpath not in bestXpaths:
            bestXpaths.append(bestXpath)
        #maxCount = max(outputXpaths.values())
        #bestXpaths.extend([xpath for (xpath, count) in outputXpaths.items() if count == maxCount])
    #bestXpaths = misc.unique(bestXpaths)

    #print allOutputXpaths
    print bestXpaths
    # add attributes to xpath
    A = xmlAttributes(Xs)
    abstractedXpaths = xmlXpaths.abstractXpaths(bestXpaths, Xs)
    return [A.addUniqueAttribs(xpath) for xpath in abstractedXpaths]


def testModel(url, model):
    """Use the model to extract output for a url of the same form"""
    results = []
    X = xmlXpaths(url, False, True)
    for xpath in model:
        this_result = []
        for element in X.getTree().xpath(xpath):
            text = X.getElementText(element)
            if text:
                this_result.append(text)
        results.extend(this_result)
    return results
