#
# Author: Richard Penman
# License: LGPL
# Description: 
# Model the desired information in a webpage.
#

from __future__ import nested_scopes, generators, division, absolute_import, with_statement
import sys
import os
import urllib2
import numpy
from difflib import SequenceMatcher
from . import misc
from lxml import etree, html

# ignore content from these tags
_IGNORE_TAGS = 'style', 'script', 'meta', 'link'
# merge these style tags content with parent
_MERGE_TAGS = 'br', 'font', 'a', 'b', 'i', 'em', 'u', 's', 'strong', 'big', 'small', 'tt', 'p'
# user agent to use in fetching webpages
_USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a9pre) Gecko/2007100205 Minefield/3.0a9pre'




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
    return ' '.join(text)


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


def extractXpaths(tree, element, xpaths):
    """Return a hashtable of the xpath to each text element"""
    tag = element.tag
    if type(tag) == type(str()):
        text = getElementText(element)
        if text:
            xpaths.setdefault(text, [])
            xpath = normalizeXpath(tree.getpath(element))
            xpaths[text].append(xpath)
        for child in element:
            extractXpaths(tree, child, xpaths)


def findXpaths(xpaths, output):
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
            s.set_seq1(misc.normalizeStr(key))
            LCSs.append((sum(n for (i, j, n) in s.get_matching_blocks()), xpaths[key]))
        lens = [l for (l, s) in LCSs]
        minLen = numpy.mean(lens) + 3*numpy.std(lens)
        return reduceXpaths(misc.flatten([s for (l, s) in LCSs if l > minLen]), [])


def reduceXpaths(xpaths, trees):
    """Reduce list of xpaths by combining similar ones in regular expressions

    >>> reduceXpaths(['/html/table/tr[1]/td', '/html/table/tr[2]/td', '/html/table/tr[3]/td', '/html/body/a'], [])
    ['/html/body/a', '/html/table/*/td']
    """
    # the xpaths that have been abstracted by a regular expression
    reducedXpaths = xpaths[:]
    #regRange = {}
    newRegs = []

    for x1 in xpaths:
        x1tokens = x1.split('/')
        for x2 in xpaths:
            if x1 != x2 and (x1 in reducedXpaths or x2 in reducedXpaths):
                x2tokens = x2.split('/')
                diff = misc.difference(x1tokens, x2tokens)
                if len(diff) == 1:
                    reg = '/'.join(x1tokens[:diff[0]] + ['*'] + x1tokens[diff[0]+1:])
                    newRegs.append(reg)

    for reg in misc.unique(newRegs):
        matchedXpaths = []
        matchedTagIds = []
        regTokens = reg.split('/')
        for xpath in reducedXpaths:
            xpathTokens = xpath.split('/')
            diff = misc.difference(regTokens, xpathTokens)
            if len(diff) == 1:
                matchedXpaths.append(xpath)
                matchedTagIds.append(misc.extractInt(xpathTokens[diff[0]]))
        if not matchedTagIds: continue
        matchedTagIds.sort()
        minPosition = matchedTagIds[0]

        # abstract this content if:
        #   there are a different number of child elements on each tree at this location
        #   or the content is ordered
        if not trees or len(misc.unique(len(tree.xpath(reg)) for tree in trees)) > 1 or \
            matchedTagIds == range(minPosition, len(matchedTagIds)+1):
            # restrict xpath regular expressions to lowest index seen
            if minPosition > 1:
                reg = reg.replace('*', '*[position()>%d]' % (minPosition - 1))
            for xpath in matchedXpaths:
                reducedXpaths.remove(xpath)
            reducedXpaths.append(reg)
    #print xpaths
    #print reducedXpaths
    return reducedXpaths


def trainModel(urlOutputs):
    """Train the model using the known output for the given urls"""
    # store relevant xpaths for each output
    outputXpaths = []
    trees = []
    for url, outputs in urlOutputs:
        tree = parseUrl(url)
        trees.append(tree)
        xpaths = {}
        extractXpaths(tree, tree.getroot(), xpaths)
        for i, output in enumerate(outputs):
            if i == len(outputXpaths): outputXpaths.append({})
            for xpath in findXpaths(xpaths, output):
                outputXpaths[i].setdefault(xpath, 0)
                outputXpaths[i][xpath] += 1

    # return most frequent xpath for each type - XXX make more robust
    bestXpaths = [misc.sortDict(x)[-1] for x in outputXpaths]
    #print outputXpaths
    #print bestXpaths
    # these xpaths form part of the total content and need to be collapsed in output
    collapseXpaths = [xpath for xpath in bestXpaths if '*' in xpath]
    return [(xpath, xpath in collapseXpaths) for xpath in reduceXpaths(bestXpaths, trees)]


def testModel(url, model):
    """Use the model to extract output for a url of the same form"""
    results = []
    tree = parseUrl(url)
    for xpath, partialContent in model:
        this_result = []
        for element in tree.xpath(xpath):
            #print 'text:', result.text
            #print result.text_content()
            #print 'children:', list(result)
            text = getElementText(element)
            if text:
                this_result.append(text)
        if partialContent:
            results.append(' '.join(this_result))
        else:
            results.extend(this_result)
    return results
