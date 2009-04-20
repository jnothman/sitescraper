import os
import re
from StringIO import StringIO
from difflib import SequenceMatcher
from lxml import html as lxmlHtml
from misc import normalizeStr, sortDict, extractInt, unique
from HtmlXpath import HtmlXpath



class HtmlDoc(object):
    """Encapsulates the Xpaths of an XML document

    >>> doc = HtmlDoc('file:data/html/search/yahoo/1.html')
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
    #MERGE_TAGS = 'br', 'font', 'b', 'i', 'em', 'u', 's', 'strong', 'big', 'small', 'tt'
    # user agent to use in fetching webpages
    USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a9pre) Gecko/2007100205 Minefield/3.0a9pre'

    def __init__(self, input, tree=False, xpaths=False):
        """Create an ElementTree of the parsed input. Input can be a url, filepath, or html"""
        if not input:
            # empty input
            url = 'input was empty'
            fp = None
        elif os.path.exists(input):
            # input is a local file
            url = input
            fp = open(url)
        elif re.match('http://.*\..*', input):
            # input is a url
            url = input
            fp = urllib2.urlopen(urllib2.Request(url, None, {'User-agent': HtmlDoc.USER_AGENT}))
        else:
            # try treating input as HTML
            url = 'input was HTML'
            fp = StringIO(input)

        self.setUrl(url)
        if fp:
            tree = lxmlHtml.parse(fp)
        else:
            tree = None
        self.setTree(tree)

        if not xpaths:
            xpaths = {}
            self.extractXpaths(self.getTree().getroot(), xpaths)
        self.setXpaths(xpaths)
        self.sequence = SequenceMatcher()#lambda x: x in ' \t\r\n')
        

    def __len__(self):
        return len(self.getXpaths())

    def __str__(self):
        return lxmlHtml.tostring(self.getTree())

    def getUrl(self):
        return self._url
    def setUrl(self, url):
        self._url = url

    def getTree(self):
        return self._tree
    def setTree(self, tree):
        self._tree = tree
        # Remove tags that are not useful
        for tag in HtmlDoc.IGNORE_TAGS:
            for item in self.getTree().findall('.//' + tag):
                item.drop_tree()

    def getXpaths(self):
        return self._xpaths
    def setXpaths(self, xpaths):
        self._xpaths = xpaths


    def extractXpaths(self, e, xpaths):
        """Return a hashtable of the xpath to each text element"""
        text = self.getElementText(e)
        xpath = HtmlXpath(self.getTree().getpath(e)).normalize()
        if text:
            if text in xpaths and xpath in xpaths[text]:
                raise Exception('duplicate: %s %s' % (xpath, text))
            xpaths.setdefault(text, [])
            xpaths[text].append(xpath)

        childTags = {}#'*': 2}
        for child in e:
            if type(child.tag) == type(str()):
                self.extractXpaths(child, xpaths)
                childTags.setdefault(child.tag, 0)
                childTags[child.tag] += 1

        # add child text content for all tags
        for childTag, count in childTags.items():
            if count >= 2:
                # add text content for this tag
                #for sep in ('/', '//'):
                childXpath = HtmlXpath('%s/%s' % (xpath, childTag))
                childText = ' '.join(self.getElementsText(e.xpath(childXpath.get())))
                if childText:
                    xpaths.setdefault(childText, [])
                    xpaths[childText].append(childXpath)


    def getElementText(self, e):
        """Extract text from HtmlElement"""
        return normalizeStr(e.text_content().strip())
        """
        text = []
        if e.text:
            text.append(e.text)
        for child in e:
            #if child.tag in HtmlDoc.MERGE_TAGS:
            #    text.append(child.text_content())
            if child.tail:
                text.append(child.tail)
        return normalizeStr(''.join(text).strip())
        """
    def getElementsText(self, es):
        return [text for text in [self.getElementText(e) for e in es]]

    def getElementHTML(self, e):
        """Extract HTML under this element"""
        return  e.text if e.text else '' + \
                ''.join([lxmlHtml.tostring(c) for c in e.getchildren()]) + \
                e.tail if e.tail else ''
    def getElementsHTML(self, es):
        return [html for html in [self.getElementHTML(e) for e in es]]


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
        >>> doc = HtmlDoc('', True, True)
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

    """def removeStatic(docs):
        ""Remove content that is static and so appears across all documents""
        if len(docs) > 1:
            for text, xpaths in docs[0].getXpaths().items():
                if all((text, xpaths) in doc.getXpaths().items() for doc in docs):
                    for doc in docs:
                        doc.getXpaths().pop(text)
    removeStatic = staticmethod(removeStatic)"""

    def removeRedundant(xpaths, docs):
        """Reduce xpath list by replacing similar xpaths with a regular expression

        >>> doc = HtmlDoc('file:data/html/search/yahoo/1.html')
        >>> xpaths = [HtmlXpath('/html[1]/table[1]/tr[1]/td[1]'), HtmlXpath('/html[1]/table[1]/tr[2]/td[1]'), HtmlXpath('/html[1]/table[1]/tr[3]/td[1]'), HtmlXpath('/html[1]/body[1]/a[1]')]
        >>> [x.get() for x in HtmlDoc.removeRedundant(xpaths, [doc])]
        ['/html[1]/body[1]/a[1]', '/html[1]/table[1]/tr/td[1]']
        """
        proposedXpathREs = HtmlXpath.abstractSet(xpaths)
        acceptedXpathREs = []
        # Try most common regular expressions first to bias towards them
        for xpathREstr, partition in sortDict(proposedXpathREs, reverse=True):
            xpathRE = HtmlXpath(xpathREstr)
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
