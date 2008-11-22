#
# Author: Richard Penman
# License: LGPL
# Description: 
# Model the desired information in a webpage
#

from __future__ import division, absolute_import
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
DEBUG = 0


class htmlXpath(object):
    """Encapsulate an xpath

    >>> x = htmlXpath('/html/body//a')
    >>> x[1]
    'body'
    >>> x[2] = 'p[1]'
    >>> x.get()
    '/html/body//p[1]'
    >>> list(x)
    ['html', 'body', 'p[1]']
    """
    sepRE = re.compile('/+')

    def __init__(self, xpathStr):
        self.set(xpathStr)

    def __len__(self):
        return len(self.sections())

    def __getitem__(self, i):
        return self.sections()[i]
    def __setitem__(self, i, v):
        xpath = self.get()
        starts, ends = [], []
        for j, match in enumerate(re.finditer(htmlXpath.sepRE, xpath)):
            starts.append(match.end())
            if match.start() > 0:
                ends.append(match.start())
            if j > i: 
                break
        ends.append(len(xpath))
        self.set(xpath[:starts[i]] + v + xpath[ends[i]:])
        return self

    def __iter__(self):
        return self.sections().__iter__()

    def __str__(self):
        return self.get()

    def __eq__(self, other):
        return self.get() == other.get()

    def copy(self):
        return htmlXpath(self.get())

    def get(self): 
        return self._xpathStr

    def set(self, xpathStr): 
        self._xpathStr = xpathStr
        return self

    def sections(self):
        """Return sections of xpath

        >>> htmlXpath('/a/b/c').sections()
        ['a', 'b', 'c']
        >>> htmlXpath('/a[1]/b').sections()
        ['a[1]', 'b']
        >>> htmlXpath('/a/b//c').sections()
        ['a', 'b', 'c']
        """
        return re.split(htmlXpath.sepRE, self.get())[1:]

    def tags(self):
        """Return list of tags in xpath
        
        >>> htmlXpath('/a/b[1]//c').tags()
        ['a', 'b', 'c']
        """
        removeIndex = lambda s: '[' in s and s[:s.index('[')] or s
        return [removeIndex(s) for s in self.sections()]

    def walk(self):
        """Return list of sub xpaths

        >>> htmlXpath('/a/b/c').walk()
        ['/a', '/a/b', '/a/b/c']
        >>> htmlXpath('/a[1]/b').walk()
        ['/a[1]', '/a[1]/b']
        >>> htmlXpath('/a/b//c').walk()
        ['/a', '/a/b', '/a/b//c']
        """
        xpaths = []
        for match in re.finditer(htmlXpath.sepRE, self.get()):
            end = match.start()
            if end > 0:
                xpaths.append(self.get()[:end])
        xpaths.append(self.get())
        return xpaths


    def normalize(self):
        """A normalized xpath has an index defined at each node. ElementTree treats indexless nodes as a regular expression.
        
        >>> htmlXpath("/a[1]/b/c[@id='2']/d").normalize().get()
        "/a[1]/b[1]/c[@id='2']/d[1]"
        """
        for i, section in enumerate(self):
            if section != '*' and not section.endswith(']'):
                self[i] = section + '[1]'
        return self

    def isNormalized(self):
        """
        >>> htmlXpath('/a[1]/b[2]').isNormalized()
        True
        >>> htmlXpath('/a[1]/b').isNormalized()
        False
        >>> htmlXpath('/a[1]//b[2]').isNormalized()
        False
        """
        if anyIn(['*', '//'], self.get()):
            return False
        else:
            return self.copy().normalize() == self

    def isAllContent(self):
        """xpaths with '//' as a separator will return all sub nodes

        >>> htmlXpath('/a[1]/b/c').isAllContent()
        False
        >>> htmlXpath('/a[1]/b//c').isAllContent()
        True
        """
        return '//' in self.get()

    def diff(self, other):
        """Returns indices where xpaths differ. Return all indices if are different length.

        >>> htmlXpath('/a/c/c').diff(htmlXpath('/a/b/c'))
        [1]
        >>> htmlXpath('/a/b/c').diff(htmlXpath('/a/b/c/d/e'))
        [0, 1, 2]
        """
        indices = []
        if self != other:
            force = self.isAllContent() != other.isAllContent() or len(self) != len(other)
            for i, (v1, v2) in enumerate(zip(self, other)):
                if force or v1 != v2:
                    indices.append(i)
            #indices.extend(range(i+1, max(len(self), len(other))))
        return indices

    def abstractSet(xpaths):
        """Abstract set of xpaths with regular expressions
        Return a dictionary with each abstracted xpath and the number of original xpaths that match
        
        >>> xpaths = []
        >>> xpaths.append(htmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/p[1]/span[1]/p[1]/strong[1]'))
        >>> xpaths.append(htmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[1]/h3[1]/a[1]'))
        >>> xpaths.append(htmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/div[1]/h3[1]/a[1]'))
        >>> xpaths.append(htmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/div[1]/h3[1]/a[1]'))
        >>> xpaths.append(htmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[2]'))
        >>> xpaths.append(htmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/div[2]'))
        >>> xpaths.append(htmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/div[2]'))
        >>> xpaths.append(htmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/span[1]'))
        >>> xpaths.append(htmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/span[1]'))
        >>> xpaths.append(htmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/span[1]'))
        >>> [x for (x, partition) in sortDict(htmlXpath.abstractSet(xpaths), reverse=True)[:5]]
        ['/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/span[1]', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/div[2]', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/div[1]/h3[1]/a[1]', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/*', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/*']
        """
        xpathREstrs = {}
        for xpath1 in xpaths:
            for xpath2 in xpaths:
                if xpath1 != xpath2:
                    diff = xpath1.diff(xpath2)
                    if len(diff) == 1:
                        partition = diff[0]
                        # use common element if possible, else '*' to match any
                        x1pathTag = xpath1.tags()[partition]
                        if x1pathTag == xpath2.tags()[partition]:
                            abstraction = x1pathTag
                        else:
                            abstraction = '*'
                        xpathRE = xpath1.copy()
                        xpathRE[partition] = abstraction
                        xpathREstr = xpathRE.get()
                        xpathREstrs.setdefault((xpathREstr, partition), 0)
                        xpathREstrs[(xpathREstr, partition)] += 1
        return xpathREstrs
    abstractSet = staticmethod(abstractSet)



class htmlDoc(object):
    """Encapsulates the Xpaths of an XML document

    >>> doc = htmlDoc('file:data/html/search/yahoo/1.html')
    >>> xpaths = {}
    >>> doc.extractXpaths(doc.getTree().getroot(), xpaths)
    >>> len(xpaths)
    438
    >>> [(xpath.get(), count) for (xpath, count) in doc.matchXpaths("Bargain prices on Digital Cameras, store variety for Digital Cameras. Compare prices and buy online at Shopzilla.")]
    [('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[2]', -113)]
    """

    # ignore content from these tags
    IGNORE_TAGS = 'style', 'script', 'meta', 'link'
    # merge these style tags content with parent
    MERGE_TAGS = 'br', 'font', 'a', 'b', 'i', 'em', 'u', 's', 'strong', 'big', 'small', 'tt'
    # user agent to use in fetching webpages
    USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a9pre) Gecko/2007100205 Minefield/3.0a9pre'


    def __init__(self, url, tree=False, xpaths=False, aggressive=False):
        self.setUrl(url)
        self.setAggressive(aggressive)
        if not tree:
            tree = self.parseUrl()
        self.setTree(tree)
        if not xpaths:
            xpaths = {}
            self.extractXpaths(self.getTree().getroot(), xpaths)
        self.setXpaths(xpaths)
        self.sequence = SequenceMatcher()#lambda x: x in ' \t\r\n')
        

    def __len__(self):
        return len(self.getXpaths())

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
    # is the doc is aggressive then the xpath parsing will be more thorough and include regular expressions and text content
    def getAggressive(self):
        return self._aggressive
    def setAggressive(self, aggressive):
        self._aggressive = aggressive

    def parseUrl(self):
        """Fetch url and return an ElementTree of the parsed XML"""
        fp = urllib2.urlopen(urllib2.Request(self.getUrl(), None, {'User-agent': htmlDoc.USER_AGENT}))
        tree = lxmlHtml.parse(fp)
        # remove tags that are not useful
        if self.getAggressive():
            for tag in htmlDoc.IGNORE_TAGS:
                for item in tree.findall('.//' + tag):
                    item.drop_tree()
        return tree


    def render(self):
        return lxmlHtml.tostring(self.getTree())


    def extractXpaths(self, e, xpaths):
        """Return a hashtable of the xpath to each text element"""
        text = self.getElementText(e)
        xpath = htmlXpath(self.getTree().getpath(e)).normalize()
        if text:
            if text in xpaths and xpath in xpaths[text]:
                raise Exception('duplicate: %s %s' % (xpath, text))
            xpaths.setdefault(text, [])
            xpaths[text].append(xpath)

        childTags = {'*': 2}
        for child in e:
            if type(child.tag) == type(str()):
                self.extractXpaths(child, xpaths)
                childTags.setdefault(child.tag, 0)
                childTags[child.tag] += 1

        # add child text content for all tags
        for childTag, count in childTags.items():
            if count >= 2:
                # add text content for this tag
                for sep in ('/', '//'):
                    childXpath = htmlXpath('%s%s%s' % (xpath, sep, childTag))
                    childText = ' '.join(self.getElementsText(e.xpath(childXpath.get())))
                    if childText:
                        xpaths.setdefault(childText, [])
                        xpaths[childText].append(childXpath)


    def getElementText(self, e):
        """Extract text from HtmlElement"""
        if 0 and self.getAggressive():
            return normalizeStr(e.text_content().strip())
        else:
            text = []
            if e.text:
                text.append(e.text)
            for child in e:
                if child.tag in htmlDoc.MERGE_TAGS:
                    text.append(child.text_content())
                if child.tail:
                    text.append(child.tail)
            return normalizeStr(''.join(text).strip())
    def getElementsText(self, es):
        return [text for text in [self.getElementText(e) for e in es] if text]

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
        >>> doc = htmlDoc('', True, True)
        >>> sorted([(doc.similarity(s, k), v) for (k, v) in matches.items()])
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

    def removeStatic(docs):
        """Remove content that is static and so appears across all documents"""
        if len(docs) > 1:
            for text, xpaths in docs[0].getXpaths().items():
                if all((text, xpaths) in doc.getXpaths().items() for doc in docs):
                    for doc in docs:
                        doc.getXpaths().pop(text)
    removeStatic = staticmethod(removeStatic)

    def removeRedundant(xpaths, docs):
        """Reduce xpath list by replacing similar xpaths with a regular expression

        >>> doc = htmlDoc('file:data/html/search/yahoo/1.html')
        >>> xpaths = [htmlXpath('/html[1]/table[1]/tr[1]/td[1]'), htmlXpath('/html[1]/table[1]/tr[2]/td[1]'), htmlXpath('/html[1]/table[1]/tr[3]/td[1]'), htmlXpath('/html[1]/body[1]/a[1]')]
        >>> [x.get() for x in htmlDoc.removeRedundant(xpaths, [doc])]
        ['/html[1]/body[1]/a[1]', '/html[1]/table[1]/tr/td[1]']
        """
        proposedXpathREs = htmlXpath.abstractSet(xpaths)
        acceptedXpathREs = []
        # Try most common regular expressions first to bias towards them
        for xpathREstr, partition in sortDict(proposedXpathREs, reverse=True):
            xpathRE = htmlXpath(xpathREstr)
            matchedXpaths = []
            matchedTags = []
            for xpath in xpaths:
                diff = xpathRE.diff(xpath)
                if len(diff) == 1:
                    matchedXpaths.append(xpath)
                    matchedTags.append(xpath[diff[0]])
            if len(matchedXpaths) < 2:
                # not enough matching xpaths to abstract
                continue 
            matchedTagIds = sorted(extractInt(tag) for tag in matchedTags)
            minPosition = matchedTagIds[0]
            # apply this regular expression if the content is ordered
            # of if there are a different number of child elements on each tree at this location
            expandReg = matchedTagIds == range(minPosition, len(matchedTagIds)+1) or \
                        len(unique([len(doc.getTree().xpath(xpathREstr)) for doc in docs])) > 1
            if expandReg:
                # restrict xpath regular expressions to lowest index encountered
                if minPosition > 1:
                    xpathRE[partition] += '[position()>%d]' % (minPosition - 1)
                acceptedXpathREs.append(xpathRE)
                # remove this xpaths now so they can't be used by another regular expression
                for xpath in matchedXpaths:
                    xpaths.remove(xpath)
        return xpaths + acceptedXpathREs
    removeRedundant = staticmethod(removeRedundant)




class htmlAttributes(object):
    """Extract attributes from XML tree and store them reverse indexed by attribute

    >>> d1 = htmlDoc('file:data/html/search/yahoo/1.html')
    >>> d2 = htmlDoc('file:data/html/search/yahoo/2.html')
    >>> d3 = htmlDoc('file:data/html/search/yahoo/3.html')
    >>> a = htmlAttributes([d1, d2, d2])
    >>> xpath = '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/span[1]'
    >>> e1 = d1.getTree().xpath(xpath)[0]
    >>> a.extractAttribs(e1)
    [('class', 'url')]
    >>> attribs = a.uniqueAttribs(htmlXpath(xpath))
    >>> attribs
    [[], [], [('id', 'doc')], [('id', 'bd')], [('id', 'results')], [('id', 'left')], [('id', 'main')], [('id', 'web')], [('start', '1')], [], [('class', 'res')], [('class', 'url')]]
    >>> a.addAttribs(htmlXpath(xpath), attribs).get()
    "/html[1]/body[1]/div[@id='doc']/div[@id='bd']/div[@id='results']/div[@id='left']/div[@id='main']/div[@id='web']/ol[@start='1']/li/div[@class='res']/span[@class='url']"

    >> tree = lxmlHtml.fromstring("<html><body node='0'><c class='1' node='1'>C<d class='2'></d></c><c class='1' node='2'>D</c></body</html>").getroottree()
    >> a = htmlAttributes(tree)
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


    def __init__(self, docs):
        self.docs = docs


    def uniqueAttribs(self, xpath):
        """Return a list of attributes that uniquely distinguish the element at each segment"""
        acceptedAttribs = []
        # select examples which contain the relevant xpath
        docs = [doc for doc in self.docs if doc.getTree().xpath(xpath.get())]
        for i, section in enumerate(xpath.walk()):
            sectionElements = flatten([doc.getTree().xpath(section) for doc in docs])
            #siblingElements = flatten([[s for s in e.itersiblings() if s.tag == e.tag] for e in sectionElements])
            #if len(siblingElements) < 0:
            if i < 2:
                # don't need to restrict html/body tags because are unique
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
        #print element.attrib.items()
        for attrName, attrValue in element.attrib.items():
            # punctuation such as '/' and ':' can confuse xpath, so ignore attributes with these characters
            if not anyIn('/:', attrValue+attrName):# and attrName in ('id', 'lass'):
                attribs.append((attrName, attrValue))
        return attribs


    def commonAttribs(self, elements):
        """Return a list of common attributes among a group of elements"""
        common = {}
        for e in elements:
            for attrib in self.extractAttribs(e):
                common.setdefault(attrib, 0)
                common[attrib] += 1
        return [attrib for (attrib, count) in common.items() if count == len(elements)]

    def addAttribs(self, xpath, allAttribs):
        """Add attributes to xpath"""
        sections = []
        for i, (section, attribs) in enumerate(zip(xpath, allAttribs)):
            if attribs:
                section = re.sub('\[\d+\]', '', section)
            for attrib in attribs:
                if type(attrib) == int:
                    section += '[%d]' % attrib
                else:
                    section += "[@%s='%s']" % attrib
            xpath[i] = section
        return xpath

    def removeAttribs(self, xpath):
        """
        >>> htmlAttributes([]).removeAttribs(htmlXpath("/a[1]/b[@class='abc']/c")).get()
        '/a[1]/b/c'
        """
        attribRE = re.compile('\[@.*?\]')
        for i, section in enumerate(xpath):
            xpath[i] = re.sub(attribRE, '', xpath[i])
        return xpath


def rankXpaths((xpath1, score1), (xpath2, score2)):
    """Rank xpaths first on score, then on all content, then on xpath length"""
    if score1 != score2:
        return score1 - score2
    elif xpath1.isAllContent() != xpath2.isAllContent():
        return xpath1.isAllContent() and -1 or 1
    else:
        return len(xpath2.get()) - len(xpath1.get())

def trainModel(urlOutputs):
    """Train the model using the known output for the given urls

    >>> from data import training
    >>> os.chdir('data')
    >>> modelSize = 3
    >>> asx = training.data[0][1][:modelSize]
    >>> trainModel(asx)
    [("/html[1]/body[1]/div[@class='a9721']/div[@id='container']/div[@id='wrap']/div[@id='content']/div[@id='col']/table[@cellspacing='0'][@class='datatable']/tr[2]/td[@class='last']", False), ("/html[1]/body[1]/div[@class='a9721']/div[@id='container']/div[@id='wrap']/div[@id='content']/div[@id='col']/table[@cellspacing='0'][@class='datatable']/tr[2]/td[6]", False), ("/html[1]/body[1]/div[@class='a9721']/div[@id='container']/div[@id='wrap']/div[@id='content']/div[@id='col']/table[@cellspacing='0'][@class='datatable']/tr[2]/td[7]", False)]
    """
    docs = [htmlDoc(url) for (url, outputs) in urlOutputs]
    htmlDoc.removeStatic(docs)

    allOutputXpathStrs = []
    # rate xpaths by the similarity of their content with the output
    for doc, (url, outputs) in zip(docs, urlOutputs):
        for i, output in enumerate(outputs):
            if i == len(allOutputXpathStrs): allOutputXpathStrs.append({})
            for xpath, score in doc.matchXpaths(normalizeStr(output)):
                xpathStr = xpath.get()
                allOutputXpathStrs[i].setdefault(xpathStr, 0)
                allOutputXpathStrs[i][xpathStr] += score

    # select best xpath match for each output
    bestXpaths = []
    for i, outputXpathStrs in enumerate(allOutputXpathStrs):
        rankedXpaths = sorted([(htmlXpath(xpathStr), score) for (xpathStr, score) in outputXpathStrs.items() if score != 0], rankXpaths)
        if rankedXpaths:
            bestXpath = rankedXpaths[0][0]
            if bestXpath not in bestXpaths:
                bestXpaths.append(bestXpath)
        if DEBUG:
            print [o[i] for (u, o) in urlOutputs if len(o) > i][0].replace('\n', '')
            for xpath, score in rankedXpaths[:5]:
                print '%6d: %s' % (score, xpath)
            print
    # store xpaths that were abstracted for a single output, and so must be collapsed together
    collapsableXpaths = [xpath for xpath in bestXpaths if not xpath.isNormalized()]
    abstractedXpaths = htmlDoc.removeRedundant(bestXpaths[:], docs)
    # replace xpath indices with attributes where possible
    A = htmlAttributes(docs)
    attributeXpathStrs = []
    for xpath in abstractedXpaths:
        collapse = xpath in collapsableXpaths or xpath.isAllContent()
        attributeXpath = A.addAttribs(xpath.copy(), A.uniqueAttribs(xpath))
        attributeXpathStrs.append((attributeXpath.get(), collapse))

    if DEBUG:
        """for i, output in enumerate(outputs):
            print
            print output
            for xpath, score in allOutputXpathStrs[i].items()[:5]:
                if score < 0:
                    print '%6d: %s' % (score, xpath)"""
        print 'C:\n', pretty(collapsableXpaths)
        print 'best:\n', pretty(bestXpaths)
        print 'abstract:\n', pretty(abstractedXpaths)
        #print 'attribute:\n', pretty(attributeXpathStrs)
    return unique(attributeXpathStrs)


def testModel(url, model):
    """Use the model to extract output for a url of the same form"""
    results = []
    doc = htmlDoc(url, False, True)
    for xpathStr, collapse in model:
        if '//' in xpathStr and collapse:
            # need to calculate sections separately to prevent collapsing unrelated parts
            base, ext = xpathStr.split('//')
            thisResults = [doc.getElementsText(e.xpath('.//' + ext)) for e in doc.getTree().xpath(base)]
        else:
            thisResults = [doc.getElementsText(doc.getTree().xpath(xpathStr))]

        for thisResult in thisResults:
            if thisResult:
                if collapse:
                    results.append(''.join(thisResult))
                else:
                    results.extend(thisResult)
            else:
                results.append('<NO MATCH>')
    return results
