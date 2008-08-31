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
from lxml import etree, html
import misc

# ignore content from these tags
_IGNORED_TAGS = 'style', 'script', 'meta', 'link'
# merge these style tags content with parent
_MERGED_TAGS = 'br', 'font', 'a', 'b', 'i', 'em', 'u', 's', 'strong', 'big', 'small', 'tt', 'p'
# user agent to use in fetching webpages
_USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a9pre) Gecko/2007100205 Minefield/3.0a9pre'


def sortDict(d):
    """Sort dictionary keys by their values

    >>> sortDict({"Richard": 23, "Andrew": 21, "James": 15})
    ['James', 'Andrew', 'Richard']
    """
    e = d.keys()
    e.sort(cmp=lambda a,b: cmp(d[a],d[b]))
    return e


def parseUrl(url):
    """Fetch url and return an ElementTree of the parsed XML"""
    fp = urllib2.urlopen(urllib2.Request(url, None, {'User-agent': _USER_AGENT}))
    tree = html.parse(fp)
    # remove style content that will confuse parsing
    for tag in _MERGED_TAGS:
        for item in tree.findall('.//' + tag):
            item.drop_tag()
    return tree


def getElementText(e):
    """Extract text from HtmlElement"""
    return (e.text.strip() if e.text else '') + ''.join(' ' + c.tail.strip() for c in e if c.tail)


def normalizeXpath(xpath):
    """ElementTree can get confused when there is no explicit index, so add where missing

    >>> normalizeXpath('/html/body/div/table[2]/tr/td/div[2]/*/div')
    /html[1]/body[1]/div[1]/table[2]/tr[1]/td[1]/div[2]/*/div[1]
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
        if tag not in _IGNORED_TAGS:
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
        for key in xpaths:
            LCSs.append((misc.lcs_len(output, key), xpaths[key]))
        lens = [l for (l, s) in LCSs]
        minLen = numpy.mean(lens) + 3*numpy.std(lens)
        #print minLen, sorted(LCSs, reverse=True)[:10]
        return reduceXpaths(misc.flatten([s for (l, s) in LCSs if l > minLen]), [])


def reduceXpaths(xpaths, trees):
    """Reduce list of xpaths by combining similar ones in regular expressions

    >>> reduceXpaths(['/html/table/tr[1]/td', '/html/table/tr[2]/td', '/html/table/tr[3]/td', '/html/body/a'], [])
    ['/html/body/a', '/html/table/*/td']
    """
    # the xpaths that have been abstracted by a regular expression
    reducedXpaths = xpaths[:]
    # regular expressions generated from xpaths
    regs = []

    for x1 in xpaths:
        x1tokens = x1.split('/')
        for x2 in xpaths:
            if x1 != x2 and (x1 in reducedXpaths or x2 in reducedXpaths):
                x2tokens = x2.split('/')
                diff = misc.difference(x1tokens, x2tokens)
                if len(diff) == 1:
                    reg = '/'.join(x1tokens[:diff[0]] + ['*'] + x1tokens[diff[0]+1:])
                    if not trees or len(misc.unique(len(tree.xpath(reg)) for tree in trees)) > 1:
                        # the trees have a different number of child elements at this node
                        #  - so get all of them
                        if reg not in reducedXpaths:
                            reducedXpaths.append(reg)
                        if x1 in reducedXpaths:
                            reducedXpaths.remove(x1)
                        if x2 in reducedXpaths:
                            reducedXpaths.remove(x2)
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
    bestXpaths = [sortDict(x)[-1] for x in outputXpaths]
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



if __name__ == '__main__':
    modelSize = 3
    from tests import *
    os.chdir('tests')
    for site, d in sorted(data.items()):
        model = trainModel(d[:modelSize])
        print site, 'model:', model
        for url, expectedOutput in d:#[modelSize:]:
            generatedOutput = testModel(url, model)
            #print "Expected:", expectedOutput
            #print "Get:", generatedOutput
            """for i, e in enumerate(expectedOutput):
                try:
                    g = generatedOutput[i]
                except IndexError:
                    g = ''
                print '%d/%d' % (lcs_len(e, g), len(normalize_str(e))),"""
            print
            for e in expectedOutput:
                for g in generatedOutput:
                    print '%d/%d' % (misc.lcs_len(e, g), len(misc.normalize_str(e))),
                print
            #print expectedOutput
            #print
            #print generatedOutput
        break
