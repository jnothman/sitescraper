#
# Author: Richard Penman
# License: LGPL
# Description: 
# Model the desired information in a webpage
#

from __future__ import nested_scopes, generators, division, absolute_import, with_statement
import sys
import os
import re
import string
import urllib2
from difflib import SequenceMatcher

currentDir = os.path.abspath(os.path.dirname(__file__))
if currentDir not in sys.path:
    sys.path.insert(0, currentDir)
from misc import normalizeStr, flatten, unique, difference, sortDict, extractInt, anyIn, allIn, pretty
from lxml import html as lxmlHtml

UNDEFINED = -1
DEBUG = False


class xmlXpaths(object):
    """Encapsulates the Xpaths of an XML document

    >>> X = xmlXpaths('file:data/html/search/yahoo/1.html')
    >>> X.normalizeXpath('/html/body/div/table[2]/tr/td/div[2]/*/div')
    '/html[1]/body[1]/div[1]/table[2]/tr[1]/td[1]/div[2]/*/div[1]'
    >>> xpaths = {}
    >>> X.extractXpaths(X.getTree().getroot(), xpaths)
    >>> len(xpaths)
    132
    >>> xpath = '/html/body/div/div[2]/div[2]/div[2]/div/div[3]/ol[1]/li/div[1]/span[1]'
    >>> xpath = X.normalizeXpath(xpath)
    >>> xpath
    '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/span[1]'
    >>> e = X.getTree().xpath(xpath)[0]
    >>> X.getElementText(e)
    'www.shopzilla.com/10J--Digital_Cameras_-_cat_id--402'
    >>> X.matchXpaths("Bargain prices on Digital Cameras, store variety for Digital Cameras. Compare prices and buy online at Shopzilla.")
    [('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[2]', 12769)]
    """

    # ignore content from these tags
    IGNORE_TAGS = 'style', 'script', 'meta', 'link'
    # merge these style tags content with parent
    MERGE_TAGS = 'br', 'font', 'a', 'b', 'i', 'em', 'u', 's', 'strong', 'big', 'small', 'tt'
    # user agent to use in fetching webpages
    USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a9pre) Gecko/2007100205 Minefield/3.0a9pre'


    def __init__(self, url, tree=False, xpaths=False):
        self.setUrl(url)
        if not tree:
            tree = self.parseUrl()
        self.setTree(tree)
        if not xpaths:
            xpaths = {}
            self.extractXpaths(self.getTree().getroot(), xpaths)
        self.setXpaths(xpaths)
        self.sequence = SequenceMatcher()#lambda x: x in ' \t\r\n')
        

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
        tree = lxmlHtml.parse(fp)
        # remove tags that are not useful
        for tag in xmlXpaths.IGNORE_TAGS:
            for item in tree.findall('.//' + tag):
                item.drop_tree()
        return tree


    def render(self):
        return lxmlHtml.tostring(self.getTree())


    def extractXpaths(self, e, xpaths):
        """Return a hashtable of the xpath to each text element"""
        text = self.getElementText(e)
        xpath = self.normalizeXpath(self.getTree().getpath(e))
        if text:
            if text in xpaths and xpath in xpaths[text]:
                raise Exception('duplicate: %s %s' % (xpath, text))
            xpaths.setdefault(text, [])
            xpaths[text].append(xpath)
        childTags = {}
        for child in e:
            childTag = child.tag
            if type(childTag) == type(str()):
                childTags.setdefault(childTag, 0)
                childTags[childTag] += 1
                if childTags[childTag] == 2:#XXX
                    childText = ''.join(self.getElementText(c) for c in e if c.tag == childTag)
                    xpaths.setdefault(childText, [])
                    childXpath = '%s/%s' % (xpath, childTag)
                    xpaths[childText].append(childXpath)
                self.extractXpaths(child, xpaths)


    def getElementText(self, e):
        """Extract text from HtmlElement"""
        #return e.text_content()
        text = []
        if e.text:
            text.append(e.text)
        for child in e:
            if child.tag in xmlXpaths.MERGE_TAGS:
                text.append(child.text_content())
            if child.tail:
                text.append(child.tail)
        return normalizeStr(''.join(text).strip())


    def normalizeXpath(self, xpath):
        """ElementTree will treat an element as a regular expression if there is no explicit index, so add where missing"""
        newXpath = []
        for tag in xpath.split('/'):
            newXpath.append(tag)
            if tag and tag != '*' and not tag.endswith(']'):
                newXpath[-1] += '[1]'
        return '/'.join(newXpath)
    def isNormalized(self, xpath):
        return xpath == self.normalizeXpath(xpath)


    def matchXpaths(self, output):
        """Return the amount of overlap at xpath with the desired output""" 
        allXpaths = self.getXpaths()
        if output in allXpaths:
            # exact match so can return xpaths directly with a perfect match
            return [(xpath, self.similarity(output, output)) for xpath in allXpaths[output]]
        else:
            # no exact match so return similarities of xpaths
            result = []
            for (text, xpaths) in allXpaths.items():
                score = self.similarity(output, text)
                result.extend((xpath, score) for xpath in xpaths)
            return result


    def similarity(self, s1, s2):
        """
        >>> s = 'hello world'
        >>> matches = {'I say now, hello world!': 1, 'ello orld': 2, 'hello': 3, 'hello world': 4, '': 5}
        >>> X = xmlXpaths('', True, True)
        >>> sorted([(X.similarity(s, k), v) for (k, v) in matches.items()])
        [(-11, 4), (-7, 2), (1, 1), (1, 3), (11, 5)]
        """
        margin = 5
        power = 1
        if len(s1)/margin < len(s2) < len(s1)*margin: 
            s = self.sequence
            if s.a != s1:
                s.set_seq1(s1)
            if s.b != s2:
                s.set_seq2(s2)
            score = 0
            for tag, i1, i2, j1, j2 in s.get_opcodes():
                thisScore = max(i2 - i1, j2 - j1)**power
                if tag == 'equal':
                    score -= thisScore
                else:
                    score += thisScore
        else:
            # don't bother calculating if string lengths are too far off, just give maximum difference
            score = abs(len(s1) - len(s2))**power
        return score

    def abstractXpaths(xpaths):
        """Abstract xpaths with regular expressions. 
        Return a dictionary with each abstracted xpath and the number of original xpaths that match
        
        >>> xmlXpaths.abstractXpaths(['/html[1]/table[1]/tr[1]/td[1]', '/html[1]/table[1]/tr[2]/td[1]', '/html[1]/table[1]/tr[3]/td[1]', '/html[1]/body[1]/a[1]'])
        {('/html[1]/table[1]/tr/td[1]', 3): 6}
        """
        regs = {}
        # remove index from tag to expose tag type
        removeIndex = lambda e: '[' in e and e[:e.index('[')] or e
        for x1 in xpaths:
            x1tokens = x1.split('/')
            for x2 in xpaths:
                if x1 != x2:
                    x2tokens = x2.split('/')
                    diff = difference(x1tokens, x2tokens)
                    if len(diff) == 1:
                        partition = diff[0]
                        # use common element if possible, else '*' to match any
                        tag1 = removeIndex(x1tokens[partition])
                        if tag1 == removeIndex(x2tokens[partition]):
                            abstraction = tag1
                        else:
                            abstraction = '*'
                        reg = '/'.join(x1tokens[:partition] + [abstraction] + x1tokens[partition+1:])
                        regs.setdefault((reg, partition), 0)
                        regs[(reg, partition)] += 1
        return regs
    abstractXpaths = staticmethod(abstractXpaths)


    def reduceXpaths(xpaths, Xs):
        """Reduce xpath list by replacing similar xpaths with a regular expression

        >>> X = xmlXpaths('file:data/html/search/yahoo/1.html')
        >>> xmlXpaths.reduceXpaths(['/html[1]/table[1]/tr[1]/td[1]', '/html[1]/table[1]/tr[2]/td[1]', '/html[1]/table[1]/tr[3]/td[1]', '/html[1]/body[1]/a[1]'], [X])
        ['/html[1]/body[1]/a[1]', '/html[1]/table[1]/tr/td[1]']
        """
        proposedRegs = xmlXpaths.abstractXpaths(xpaths)
        acceptedRegs = []
        # Try most common regular expressions first to bias towards them
        for reg, partition in sortDict(proposedRegs, reverse=True):
            matchedXpaths = []
            matchedTags = []
            regTokens = reg.split('/')
            for xpath in xpaths:
                xpathTokens = xpath.split('/')
                diff = difference(regTokens, xpathTokens)
                if len(diff) == 1:
                    matchedXpaths.append(xpath)
                    matchedTags.append(xpathTokens[diff[0]])
            if len(matchedXpaths) < 2:
                # not enough matching xpaths to abstract
                continue 
            matchedTagIds = sorted(extractInt(tag) for tag in matchedTags)
            minPosition = matchedTagIds[0]

            # apply this regular expression if the content is ordered
            # of if there are a different number of child elements on each tree at this location
            expandReg = (matchedTagIds == range(minPosition, len(matchedTagIds)+1)) or \
                        (len(unique(len(X.getTree().xpath(reg)) for X in Xs)) > 1)
            if expandReg:
                # restrict xpath regular expressions to lowest index encountered
                if minPosition > 1:
                    regTokens[partition] += '[position()>%d]' % (minPosition - 1)
                reg = '/'.join(regTokens)
                # remove this xpaths now so they can't be used by another regular expression
                for xpath in matchedXpaths:
                    xpaths.remove(xpath)
                acceptedRegs.append(reg)
        return xpaths + acceptedRegs
    reduceXpaths = staticmethod(reduceXpaths)


    def breakXpath(xpath):
        """Break xpath into tag sections

        >>> xmlXpaths.breakXpath('/a/b/c')
        ['/a', '/a/b', '/a/b/c']
        """
        xpaths = []
        sections = xpath.split('/')
        for i in range(1, len(sections)):
            xpaths.append('/'.join(sections[:i+1]))
        return xpaths
    breakXpath = staticmethod(breakXpath)




class xmlAttributes(object):
    """Extract attributes from XML tree and store them reverse indexed by attribute

    >>> X1 = xmlXpaths('file:data/html/search/yahoo/1.html')
    >>> X2 = xmlXpaths('file:data/html/search/yahoo/2.html')
    >>> X3 = xmlXpaths('file:data/html/search/yahoo/3.html')
    >>> a = xmlAttributes([X1, X2, X2])
    >>> xpath = '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/span[1]'
    >>> e1 = X1.getTree().xpath(xpath)[0]
    >>> a.extractAttribs(e1)
    [('class', 'url')]
    >>> attribs = a.uniqueAttribs(xpath)
    >>> attribs
    [[], [], [], [], [('id', 'bd')], [], [('id', 'left')], [], [('id', 'web')], [], [], [], [('class', 'url')]]
    >>> a.addAttribs(xpath, attribs)
    "/html[1]/body[1]/div[1]/div[@id='bd']/div[2]/div[@id='left']/div[1]/div[@id='web']/ol[1]/li/div[1]/span[@class='url']"

    >> tree = lxmlHtml.fromstring("<html><body node='0'><c class='1' node='1'>C<d class='2'></d></c><c class='1' node='2'>D</c></body</html>").getroottree()
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
        for section in xmlXpaths.breakXpath(xpath):
            sectionElements = flatten([X.getTree().xpath(section) for X in Xs])
            siblingElements = flatten([[s for s in e.itersiblings() if s.tag == e.tag] for e in sectionElements])
            if len(siblingElements) == 0:
                # element has no siblings so no need to restrict
                proposedAttribs = []
            else:
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
                            if allIn(proposedAttribs, e.attrib.items()):
                                index += 1
                        else:
                            break
                sectionXpath = self.addAttribs(section, section.count('/')*[[]] + [proposedAttribs])
                print int(round(index // len(Xs))), sectionXpath, [X.getTree().xpath(sectionXpath) for X in Xs]
                #proposedAttribs.append(index)"""
            acceptedAttribs.append(proposedAttribs)
        return acceptedAttribs


    def extractAttribs(self, element):
        """Return a list of attributes for the element"""
        attribs = []
        for attrib in element.attrib.items():
            attrName, attrValue = attrib
            # punctuation such as '/' and ':' can confuse xpath, so ignore these attributes
            if not anyIn(string.punctuation, attrValue+attrName):# and attrName in ('id', 'class'):
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

    def removeAttribs(self, xpath):
        """
        >>> xmlAttributes([]).removeAttribs("/html[1]/body/a[2][@id='2'][@class='down']/b")
        '/html[1]/body/a[2]/b'
        """
        return re.sub('\[@.*?\]', '', xpath)


def trainModel(urlOutputs):
    """Train the model using the known output for the given urls"""
    Xs = [xmlXpaths(url) for (url, outputs) in urlOutputs]
    allOutputXpaths = []
    # rate xpaths by the similarity of their content with the output
    for X, (url, outputs) in zip(Xs, urlOutputs):
        for i, output in enumerate(outputs):
            if i == len(allOutputXpaths): allOutputXpaths.append({})
            for xpath, score in X.matchXpaths(normalizeStr(output)):
                allOutputXpaths[i].setdefault(xpath, 0)
                allOutputXpaths[i][xpath] += score
                if score < 0:
                    pass
                    #print xpath, score, allOutputXpaths[i][xpath]

    # select best xpath match for each output
    bestXpaths = []
    for outputXpaths in allOutputXpaths:
        rankedXpaths = sorted([(score, 1/float(len(xpath)), xpath) for (xpath, score) in outputXpaths.items()])
        bestXpath = rankedXpaths[0][-1]
        if bestXpath not in bestXpaths:
            bestXpaths.append(bestXpath)

    # store xpaths that were abstracted for a single output, and so must be collapsed together
    collapsableXpaths = [xpath for xpath in bestXpaths if not X.isNormalized(xpath)]
    abstractedXpaths = xmlXpaths.reduceXpaths(bestXpaths[:], Xs)
    # replace xpath indices with attributes where possible
    A = xmlAttributes(Xs)
    attributeXpaths = [(A.addUniqueAttribs(xpath), xpath in collapsableXpaths) for xpath in abstractedXpaths]

    if DEBUG:
        for i, output in enumerate(outputs):
            print
            print output
            for xpath, score in allOutputXpaths[i].items():
                if score < 0:
                    print xpath, score
        print 'C:\n', pretty(collapsableXpaths)
        print 'best:\n', pretty(bestXpaths)
        print 'abstract:\n', pretty(abstractedXpaths)
        print 'attribute:\n', pretty(attributeXpaths)
    return attributeXpaths


def testModel(url, model):
    """Use the model to extract output for a url of the same form"""
    results = []
    X = xmlXpaths(url, False, True)
    for xpath, collapse in model:
        this_result = []
        for element in X.getTree().xpath(xpath):
            text = X.getElementText(element)
            if text:
                this_result.append(text)
        if this_result:
            if collapse:
                results.append(''.join(this_result))
            else:
                results.extend(this_result)
        else:
            results.append('<NO MATCH>')
    return results
