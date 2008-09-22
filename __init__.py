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
        """ElementTree will treat an element as a regular expression if there is no explicit index, so add where missing
        
        >>> htmlXpath("/a[1]/b/c[@id='2']//d").normalize().get()
        "/a[1]/b[1]/c[@id='2']//d[1]"
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
        """
        if '*' in self.get():
            return False
        else:
            return self.copy().normalize() == self


    def diff(self, other):
        """
        >>> htmlXpath('/a/c/c').diff(htmlXpath('/a/b/c'))
        [1]
        """
        indices = []
        for i, (v1, v2) in enumerate(zip(self, other)):
            if v1 != v2:
                indices.append(i)
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
        ['/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/span[1]', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/div[2]', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/div[1]/h3[1]/a[1]', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/*', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/*']
        """
        xpathREstrs = {}
        for xpath1 in xpaths:
            if '//' in xpath1.get(): continue
            for xpath2 in xpaths:
                if '//' in xpath2.get(): continue
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
    215
    >>> [(xpath.get(), count) for (xpath, count) in doc.matchXpaths("Bargain prices on Digital Cameras, store variety for Digital Cameras. Compare prices and buy online at Shopzilla.")]
    [('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/div', -113), ('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]//div', -113), ('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[2]', -113)]
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
        fp = urllib2.urlopen(urllib2.Request(self.getUrl(), None, {'User-agent': htmlDoc.USER_AGENT}))
        tree = lxmlHtml.parse(fp)
        # remove tags that are not useful
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
        childTags = {}
        # add child text content for all tags
        for sep in ('/', '//'):
            childXpath = htmlXpath('%s%s*' % (xpath.get(), sep))
            childText = ' '.join(self.getElementsText(e.xpath(childXpath.get())))
            if childText:
                xpaths.setdefault(childText, [])
                xpaths[childText].append(childXpath)
        for child in e:
            childTag = child.tag
            if type(childTag) == type(str()):
                childTags.setdefault(childTag, 0)
                childTags[childTag] += 1
                if childTags[childTag] == 2:
                    # add text content for this tag
                    for sep in ('/', '//'):
                        childXpath = htmlXpath('%s%s%s' % (xpath, sep, childTag))
                        childText = ' '.join(self.getElementsText(e.xpath(childXpath.get())))
                        if childText:
                            xpaths.setdefault(childText, [])
                            xpaths[childText].append(childXpath)
                self.extractXpaths(child, xpaths)


    def getElementText(self, e):
        """Extract text from HtmlElement"""
        #return e.text_content()
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

    def reduceXpaths(xpaths, docs):
        """Reduce xpath list by replacing similar xpaths with a regular expression

        >>> doc = htmlDoc('file:data/html/search/yahoo/1.html')
        >>> xpaths = [htmlXpath('/html[1]/table[1]/tr[1]/td[1]'), htmlXpath('/html[1]/table[1]/tr[2]/td[1]'), htmlXpath('/html[1]/table[1]/tr[3]/td[1]'), htmlXpath('/html[1]/body[1]/a[1]')]
        >>> [x.get() for x in htmlDoc.reduceXpaths(xpaths, [doc])]
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
    reduceXpaths = staticmethod(reduceXpaths)




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
    [[], [], [], [('id', 'bd')], [], [('id', 'left')], [], [('id', 'web')], [], [], [], [('class', 'url')]]
    >>> a.addAttribs(htmlXpath(xpath), attribs).get()
    "/html[1]/body[1]/div[1]/div[@id='bd']/div[2]/div[@id='left']/div[1]/div[@id='web']/ol[1]/li/div[1]/span[@class='url']"

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
        for section in xpath.walk():
            sectionElements = flatten([doc.getTree().xpath(section) for doc in docs])
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




def trainModel(urlOutputs):
    """Train the model using the known output for the given urls
    
    >>> from data import *
    >>> os.chdir('data')
    >>> modelSize = 3
    >>> asx = data[0][1][:modelSize]
    >>> trainModel(asx)
    [("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[@id='col']/table[1]/tr[2]/td[@class='last']", False), ("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[@id='col']/table[1]/tr[2]/td[6]", False), ("/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[@id='col']/table[1]/tr[2]/td[7]", False)]
    >>> weather = data[1][1][:modelSize]
    >>> trainModel(weather)
    [("/html[1]/body[1]/div[1]/div[5]/div[6]/table[1]/tr[position()>3]/td[@class='navcon']/ul[1]/li[1]/a[1]", False)]
    >>> theage = data[2][1][:modelSize]
    >>> trainModel(theage)
    [("/html[1]/body[1]/div[@id='wrap']/div[3]/div[3]/div[@id='content']/div[@class='col1']//p", True)]
    >>> amazon = data[3][1][:modelSize]
    >>> trainModel(amazon)
    [("/html[1]/body[1]/table[@cellpadding='0'][@cellspacing='0'][@id='searchTemplate'][@border='0']/tr[1]/td[2]/div[1]/table[1]/tr/td[1]/table[1]/tr[1]/td[2]/table[1]/tr[1]/td[1]/table[1]/tr[1]/td[2]/table[1]/tr[1]/td[1]/a[1]/span[1]", False), ("/html[1]/body[1]/table[@cellpadding='0'][@cellspacing='0'][@id='searchTemplate'][@border='0']/tr[1]/td[2]/div[1]/table[1]/tr/td[1]/table[1]/tr[1]/td[2]/table[1]/tr[1]/td[1]/table[1]/tr[1]/td[2]/table[1]/tr[2]/td[1]/span[3]", False)]
    >>> imdb = data[4][1][:modelSize]
    >>> trainModel(imdb)
    [("/html[1]/body[1]/div[1]/div[@id='root']/layer[1]/div[@id='pagecontent']/div[1]/div[4]/div[@id='tn15title']/h1[1]", False), ("/html[1]/body[1]/div[1]/div[@id='root']/layer[1]/div[@id='pagecontent']/div[1]/div[4]/div[3]/div[@class='info']/table[1]/tr/td[@class='nm']/a[1]", False), ("/html[1]/body[1]/div[1]/div[@id='root']/layer[1]/div[@id='pagecontent']/div[1]/div[4]/div[3]/div[@class='info']/table[1]/tr/td[4]", False)]
    >>> yahoo = data[5][1][:modelSize]
    >>> trainModel(yahoo)
    [("/html[1]/body[1]/div[1]/div[@id='bd']/div[2]/div[@id='info']/p[1]/span[1]/p[1]/strong[1]", False), ("/html[1]/body[1]/div[1]/div[@id='bd']/div[2]/div[@id='left']/div[1]/div[@id='web']/ol[1]/li[2]/div[1]/span[1]", False), ("/html[1]/body[1]/div[1]/div[@id='bd']/div[2]/div[@id='left']/div[1]/div[@id='web']/ol[1]/li/div[1]/div[@class='abstr']", False), ("/html[1]/body[1]/div[1]/div[@id='bd']/div[2]/div[@id='left']/div[1]/div[@id='web']/ol[1]/li/div[1]/div[1]/h3[1]/a[1]", False), ("/html[1]/body[1]/div[1]/div[@id='bd']/div[2]/div[@id='left']/div[1]/div[@id='web']/ol[1]/li/div[1]/span[@class='url']", False)]
    >>> lq = data[6][1][:modelSize]
    >>> trainModel(lq)
    [("/html[1]/body[1]/div[@align='center']/div[1]/div[1]/table[2]/tr[1]/td[@class='page'][@valign='top']/div[@class='KonaBody']/div[@id='posts']/div[@align='center']/div[1]/div[1]/div[1]/table[1]/tr[@valign='top']/td[2]/div[3]", False), ("/html[1]/body[1]/div[@align='center']/div[1]/div[1]/table[2]/tr[1]/td[@class='page'][@valign='top']/div[@class='KonaBody']/div[@id='posts']/div[@align='center']/div[1]/div[1]/div[1]/table[1]/tr[@valign='top']/td[2]/div[1]", False), ("/html[1]/body[1]/div[@align='center']/div[1]/div[1]/table[2]/tr[1]/td[@class='page'][@valign='top']/div[@class='KonaBody']/div[@id='posts']/div[@align='center']/div[1]/div[1]/div[1]/table[1]/tr[@valign='top']/td[2]/div[1]/div[1]/table[1]/tr[1]/td[1]//div", True)]
    """
    docs = [htmlDoc(url) for (url, outputs) in urlOutputs]
    allOutputXpathStrs = []
    # rate xpaths by the similarity of their content with the output
    for doc, (url, outputs) in zip(docs, urlOutputs):
        for i, output in enumerate(outputs):
            if i == len(allOutputXpathStrs): allOutputXpathStrs.append({})
            for xpath, score in doc.matchXpaths(normalizeStr(output)):
                xpathStr = xpath.get()
                allOutputXpathStrs[i].setdefault(xpathStr, 0)
                allOutputXpathStrs[i][xpathStr] += score
                if score < 0:
                    pass
                    #print xpath, score, allOutputXpaths[i][xpath]

    # select best xpath match for each output
    bestXpaths = []
    for outputXpathStrs in allOutputXpathStrs:
        rankedXpaths = sorted([(score, 1/float(len(xpathStr)), htmlXpath(xpathStr)) for (xpathStr, score) in outputXpathStrs.items()])
        bestXpath = rankedXpaths[0][-1]
        if bestXpath not in bestXpaths:
            bestXpaths.append(bestXpath)

    # store xpaths that were abstracted for a single output, and so must be collapsed together
    collapsableXpaths = [xpath for xpath in bestXpaths if not xpath.isNormalized()]
    abstractedXpaths = htmlDoc.reduceXpaths(bestXpaths[:], docs)
    # replace xpath indices with attributes where possible
    A = htmlAttributes(docs)
    attributeXpathStrs = []
    for xpath in abstractedXpaths:
        collapse = xpath in collapsableXpaths
        attributeXpath = A.addAttribs(xpath.copy(), A.uniqueAttribs(xpath))
        attributeXpathStrs.append((attributeXpath.get(), collapse))

    if DEBUG:
        """for i, output in enumerate(outputs):
            print
            print output
            for xpath, score in allOutputXpaths[i].items():
                if score < 0:
                    print xpath, score"""
        print 'C:\n', pretty(collapsableXpaths)
        print 'best:\n', pretty(bestXpaths)
        print 'abstract:\n', pretty(abstractedXpaths)
        #print 'attribute:\n', pretty(attributeXpathsStrs)
    return attributeXpathStrs


def testModel(url, model):
    """Use the model to extract output for a url of the same form"""
    results = []
    doc = htmlDoc(url, False, True)
    for xpathStr, collapse in model:
        this_result = doc.getElementsText(doc.getTree().xpath(xpathStr))
        if this_result:
            if collapse:
                results.append(''.join(this_result))
            else:
                results.extend(this_result)
        else:
            results.append('<NO MATCH>')
    return results
