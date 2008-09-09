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
import urllib2
import numpy
from difflib import SequenceMatcher
from . import misc
from lxml import etree, html

# ignore content from these tags
_IGNORE_TAGS = 'style', 'script', 'meta', 'link'
# merge these style tags content with parent
_MERGE_TAGS = 'br', 'font', 'a', 'b', 'i', 'em', 'u', 's', 'strong', 'big', 'small', 'tt'#, 'p'
# user agent to use in fetching webpages
_USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a9pre) Gecko/2007100205 Minefield/3.0a9pre'

UNDEFINED = -1



def parseUrl(url):
    """Fetch url and return an ElementTree of the parsed XML"""
    fp = urllib2.urlopen(urllib2.Request(url, None, {'User-agent': _USER_AGENT}))
    tree = html.parse(fp)
    # remove tags that are not useful
    for tag in _IGNORE_TAGS:
        for item in tree.findall('.//' + tag):
            item.drop_tree()
    return tree


def getElementText(e):
    """Extract text from HtmlElement"""
    text = []
    if e.text:
        text.append(e.text.strip())
    for child in e:
        if child.tag in _MERGE_TAGS:
            text.append(child.text_content())
        if child.tail:
            text.append(child.tail.strip())
    return misc.normalizeStr(' '.join(text))

# XXX refactor xpath functions into class xmlXpath
def normalizeXpath(xpath):
    """ElementTree can get confused when there is no explicit index, so add where missing

    >>> normalizeXpath('/html/body/div/table[2]/tr/td/div[2]/*/div')
    '/html[1]/body[1]/div[1]/table[2]/tr[1]/td[1]/div[2]/*/div[1]'
    """
    newXpath = []
    for tag in xpath.split('/'):
        newXpath.append(tag)
        if tag and tag != '*' and not tag.endswith(']'):
            newXpath[-1] += '[1]'
    return '/'.join(newXpath)
def notNormalized(xpath):
    """A non-normalized xpath will have a token without an index

    >>> notNormalized('/html[1]/body[1]/div[1]/table[2]')
    []
    >>> notNormalized('/html[1]/body[1]/div/table[2]/a')
    [3, 5]
    >>> notNormalized('/html[1]/body[1]/*[position()>1]/table[2]')
    [3]
    """
    return [i for (i, tag) in enumerate(xpath.split('/')) if tag and not re.search("\[\d+\]", tag)]


def extractXpaths(tree, element = {}, xpaths = {}):
    """Return a hashtable of the xpath to each text element"""
    try:
        tag = element.tag
    except AttributeError:
        extractXpaths(tree, tree.getroot(), xpaths)
    else:
        if type(tag) == type(str()):
            text = getElementText(element)
            if text:
                xpaths.setdefault(text, [])
                xpath = normalizeXpath(tree.getpath(element))
                if xpath not in xpaths[text]:
                    xpaths[text].append(xpath)
            for child in element:
                extractXpaths(tree, child, xpaths)
    return xpaths


def matchXpaths(xpaths, tree, output):
    """Find matching xpaths of output""" 
    if output in xpaths:
        # exact match so can return xpaths directly
        return xpaths[output]
    else:
        # no exact match so return xpaths with Longest Common Sequence (LCS) 3 STDs over the mean
        LCSs = []
        s = SequenceMatcher()
        s.set_seq2(misc.normalizeStr(output))
        for key in xpaths:
            s.set_seq1(key)
            LCSs.append((sum(n for (i, j, n) in s.get_matching_blocks()), xpaths[key]))
        lens = [l for (l, xpaths) in LCSs]
        minLen = numpy.mean(lens) + 3*numpy.std(lens)
        bestXpaths = misc.flatten([xpaths for (l, xpaths) in LCSs if l > minLen])
        for i, xpath in enumerate(bestXpaths):#XXX
            e = tree.xpath(xpath)[0]
            text = getElementText(e)
            alltext = misc.normalizeStr(e.text_content())
            s.set_seq1(text)
            textLCS = sum(n for (i, j, n) in s.get_matching_blocks())
            s.set_seq1(alltext)
            alltextLCS = sum(n for (i, j, n) in s.get_matching_blocks())
            #print len(text), textLCS, len(alltext), alltextLCS, len(misc.normalizeStr(output))
        return bestXpaths


def reduceXpaths(xpaths, trees):
    """Reduce list of xpaths by combining similar ones in regular expressions

    >>> reduceXpaths(['/html[1]/table[1]/tr[1]/td[1]', '/html[1]/table[1]/tr[2]/td[1]', '/html[1]/table[1]/tr[3]/td[1]', '/html[1]/body[1]/a[1]'], [])
    ['/html[1]/body[1]/a[1]', '/html[1]/table[1]/*/td[1]']
    """
    newRegs = {}
    for x1 in xpaths:
        x1tokens = x1.split('/')
        for x2 in xpaths:
            if x1 != x2:
                x2tokens = x2.split('/')
                diff = misc.difference(x1tokens, x2tokens)
                if len(diff) == 1:
                    reg = '/'.join(x1tokens[:diff[0]] + ['*'] + x1tokens[diff[0]+1:])
                    newRegs.setdefault(reg, 0)
                    newRegs[reg] += 1

    # newRegs now holds the number of matching xpaths for each regular expression
    # so sort by this amount to favour more useful regular expressions.
    # This is important when extracting 2 columns of data from a webpage where the rows will also match
    for reg in misc.sortDict(newRegs, True):
        matchedXpaths = []
        matchedTags = []
        regTokens = reg.split('/')
        for xpath in xpaths:
            if notNormalized(xpath) == []:
                xpathTokens = xpath.split('/')
                diff = misc.difference(regTokens, xpathTokens)
                if len(diff) == 1:
                    matchedXpaths.append(xpath)
                    matchedTags.append(xpathTokens[diff[0]])
        if not matchedXpaths: 
            continue # these xpaths have already been used by a previous regular expression
        matchedTagIds = sorted(misc.extractInt(tag) for tag in matchedTags)
        minPosition = matchedTagIds[0]
        # abstract this content if:
        #   there are a different number of child elements on each tree at this location
        #   or the content is ordered
        variableLength = len(misc.unique(len(tree.xpath(reg)) for tree in trees)) > 1
        isOrdered = matchedTagIds == range(minPosition, len(matchedTagIds)+1)
        if not trees or variableLength or isOrdered:
            # restrict xpath regular expressions to lowest index encountered
            uniqueTags = misc.unique(tag[:tag.index('[')] for tag in matchedTags)
            if len(uniqueTags) > 1:
                commonTag = '*'
            else:
                commonTag = uniqueTags[0]
            if minPosition > 1:
                commonTag += '[position()>%d]' % (minPosition - 1)
            partition = notNormalized(reg)[0]
            reg = '/'.join(regTokens[:partition] + [commonTag] + regTokens[partition+1:])
            # remove this xpaths now so they can't be used by another regular expression
            for xpath in matchedXpaths:
                xpaths.remove(xpath)
            xpaths.append(reg)
    return xpaths


class xmlAttribs(object):
    """Extract attributes from XML tree and store them reverse indexed by attribute

    >>> tree = html.fromstring("<html><body node='0'><c class='1' node='1'>C<d class='2'></d></c><c class='1' node='2'>D</c></body</html>").getroottree()
    >>> a = xmlAttribs(tree)
    >>> a.breakXpath('/a/b/c')
    ['/a', '/a/b', '/a/b/c']
    >>> extractXpaths(tree)
    {'C': ['/html[1]/body[1]/c[1]'], 'D': ['/html[1]/body[1]/c[2]']}
    >>> a.extractAttribs(['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]'])
    {('node', '0'): ['/html[1]/body[1]'], ('node', '2'): ['/html[1]/body[1]/c[2]'], ('node', '1'): ['/html[1]/body[1]/c[1]'], ('class', '1'): ['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]']}
    >>> a.commonAttribs(['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]'])
    [(('node', '0'), '/html[1]/body[1]'), (('class', '1'), '/html[1]/body[1]/c[2]')]
    """
    def __init__(self, tree, xpaths=[]):
        if not xpaths:
            xpaths = misc.flatten(extractXpaths(tree).values())
        self.tree = tree
        self.attribs = self.extractAttribs(xpaths)

    def breakXpath(self, xpath):
        xpaths = []
        sections = xpath.split('/')
        for i in range(1, len(sections)):
            xpaths.append('/'.join(sections[:i+1]))
        return xpaths

    def extractAttribs(self, xpaths):
        """Return a dictionary of attributs for each xpath"""
        attribs = {}
        done = []
        for xpath in xpaths:
            sections = self.breakXpath(xpath)
            for section in sections:
                if section not in done:
                    done.append(section)
                    for element in self.tree.xpath(section):
                        for attrib in element.attrib.items():
                            attribs.setdefault(attrib, [])
                            attribs[attrib].append(section)
        return attribs

    def commonAttribs(self, xpaths):
        """Return a list of common attributes among a group of xpaths"""
        common = []
        for attrib in self.extractAttribs(xpaths):
            matchingXpaths = self.attribs[attrib]
            match = None
            for xpath in xpaths:
                match = misc.anyIn(self.breakXpath(xpath), matchingXpaths)
                if not match:
                    break
            if match: 
                common.append((attrib, match))
        return common


def trainModel(urlOutputs):
    """Train the model using the known output for the given urls"""
    # store relevant xpaths for each output
    outputXpaths = []
    trees = []
    for url, outputs in urlOutputs:
        tree = parseUrl(url)
        trees.append(tree)
        xpaths = extractXpaths(tree)
        for i, output in enumerate(outputs):
            if i == len(outputXpaths): outputXpaths.append({})
            bestXpaths = matchXpaths(xpaths, tree, output)
            for xpath in reduceXpaths(bestXpaths, []):
                outputXpaths[i].setdefault(xpath, 0)
                outputXpaths[i][xpath] += 1

    # return most frequent xpath for each type
    commonXpaths = [sorted(x for (x, count) in xs.items() if count == max(xs.values()))[0] for xs in outputXpaths]
    #print outputXpaths
    # these xpaths form part of the total content and need to be collapsed in output
    collapseXpaths = [xpath for xpath in commonXpaths if notNormalized(xpath)]
    return [(xpath, xpath in collapseXpaths) for xpath in reduceXpaths(commonXpaths, trees)]


def testModel(url, model):
    """Use the model to extract output for a url of the same form"""
    results = []
    tree = parseUrl(url)
    for xpath, partialContent in model:
        this_result = []
        for element in tree.xpath(xpath):
            text = getElementText(element)
            #text = misc.normalizeStr(element.text_content())
            if text:
                this_result.append(text)
        if partialContent:
            results.append(' '.join(this_result))
        else:
            results.extend(this_result)
    return results
