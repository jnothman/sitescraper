#
# Author: Richard Penman
# License: LGPL
# Description: 
# Model the desired information in a webpage
#

from collections import defaultdict
from HtmlDoc import HtmlDoc
from HtmlXpath import HtmlXpath
from HtmlAttributes import HtmlAttributes
from common import normalizeStr, unique, pretty, flatten, extractInt



class HtmlModel:
    def __init__(self, docs, attributes=True, debug=False):
        """
        'docs' are the HTML webpages to model
        'attributes' are whether to replace the xpath indices with attributes
        'debug' is whether to print internal information of the model generation
        """
        self._docs = docs
        self._attributes = attributes
        self._debug = debug
        self._model = None # model is not generated yet


    def get(self):
        if self._model is None:
            # need to generate model
            model = self.trainModel()
            if self._debug:
                print 'model:\n', pretty(model)
            if self._attributes:
                model = self.addAttributes(model)
                if self._debug:
                    print 'attributes:\n', pretty(model)
            self._model = []
            for xpath in model:
                record = xpath.get()
                if xpath.mode() != HtmlXpath.DEFAULT_MODE:
                    record = record, xpath.mode()
                self._model.append(record)
        return self._model


    def trainModel(self):
        """Train the model using the known output for the given urls"""
        outputScores = []
        # rate xpaths by the similarity of their content with the output
        for doc in self._docs:
            for i, output in enumerate(doc.output()):
                if i == len(outputScores): outputScores.append(defaultdict(int))
                for xpath, score in doc.matchXpaths(normalizeStr(output)):
                    outputScores[i][xpath] += score

        # select best xpath match for each output
        accurateXpaths = []
        for xpathScores in outputScores:
            # allow 0 to be the worst xpath match, which is an element that half matches
            bestScore = min([0] + [score for (xpath, score) in xpathScores.items()])
            accurateXpaths.append([xpath for (xpath, score) in xpathScores.items() if score == bestScore])
        if self._debug:
            for i, xpaths in enumerate(accurateXpaths):
                print [doc.output()[i] for doc in self._docs if len(doc) > i][0].replace('\n', '')
                print pretty(xpaths)
        return self.refineXpaths(accurateXpaths)


    def addAttributes(self, xpaths):
        """Replace xpath indices with attributes where possible"""
        A = HtmlAttributes(self._docs)
        xpathAttribStrs = []
        for xpath in xpaths:
            xpathAttribStrs.append(A.addAttribs(xpath.copy(), A.uniqueAttribs(xpath)))
        return xpathAttribStrs


    def refineXpaths(self, xpathsGroup):
        """Reduce xpath list by replacing similar xpaths with a regular expression

        >>> doc = HtmlDoc('file:test/yahoo_search/1.html', [])
        >>> xpathsGroup = [
            [HtmlXpath('/html[1]/body[1]/table[1]/tr[1]/td[1]'), HtmlXpath('/html[1]/body[1]/table[1]/tr[1]')],
            [HtmlXpath('/html[1]/body[1]/table[1]/tr[2]/td[1]'), HtmlXpath('/html[1]/body[1]/table[1]/tr[2]')],
            [HtmlXpath('/html[1]/body[1]/table[1]/tr[3]/td[1]'),],
            [HtmlXpath('/html[1]/body[1]/a[1]')],
        ]
        >>> #[xpath.get() for xpath in HtmlModel(doc).cleanXpaths(xpathsGroup)]
        >>> HtmlModel(doc).refineXpaths(xpathsGroup)
        ['/html[1]/body[1]/a[1]', '/html[1]/body[1]/table[1]/tr/td[1]']
        """
        proposedXpaths = self.abstractXpaths(xpathsGroup)
        if self._debug:
            print [(xpath.get(), count) for (xpath, count) in proposedXpaths]
        acceptedXpaths = []
        # Try most common regular expressions first to bias towards them
        for abstractXpath, partition in proposedXpaths:
            matchedXpaths = []
            matchedTags = []
            for xpaths in xpathsGroup:
                for xpath in xpaths:
                    diff = abstractXpath.diff(xpath)
                    if len(diff) == 1:
                        matchedXpaths.append(xpath)
                        matchedTags.append(xpath[diff[0]])
                        break
            if len(matchedXpaths) < 2:
                # not enough matching xpaths to abstract
                continue 

            matchedTagIds = sorted(extractInt(tag) for tag in matchedTags)
            minPosition = matchedTagIds[0]
            # apply this regular expression if the content is ordered
            # of if there are a different number of child elements on each tree at this location
            expandReg = matchedTagIds == range(minPosition, len(matchedTagIds)+1) or \
                        len(unique([len(doc.tree().xpath(abstractXpath.get())) for doc in self._docs])) > 1
            if expandReg:
                # restrict xpath regular expressions to lowest index encountered
                if minPosition > 1:
                    abstractXpath[partition] += '[position()>%d]' % (minPosition - 1)
                acceptedXpaths.append(abstractXpath)
                # remove this xpaths now so they can't be used by another regular expression
                for matchedXpath in matchedXpaths:
                    for xpaths in xpathsGroup:
                        if matchedXpath in xpaths:
                            xpathsGroup.remove(xpaths)
        if self._debug:                            
            for xpaths in xpathsGroup:
                if len(xpaths) > 1:
                    print 'not abstracted:', ', '.join([xpath.get() for xpath in xpaths])

        return [xpaths[0] for xpaths in xpathsGroup if xpaths] + acceptedXpaths
    


    def abstractXpaths(self, xpathsGroup):
        """Abstract set of xpaths using regular expressions, with most useful abstractions first in the list
        Return a dictionary with each abstracted xpath and the number of original xpaths that match
        
        >>> xpaths = []
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/p[1]/span[1]/p[1]/strong[1]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[1]/h3[1]/a[1]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/div[1]/h3[1]/a[1]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/div[1]/h3[1]/a[1]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[2]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/div[2]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/div[2]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/span[1]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/span[1]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/span[1]'))
        >>> [x for (x, partition) in sortDict(HtmlXpath.abstractSet(xpaths), reverse=True)[:5]]
        ['/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/span[1]', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/div[2]', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/div[1]/h3[1]/a[1]', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/*', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/*']
        """
        abstractXpaths = defaultdict(int)
        for xpaths1 in xpathsGroup:
            for xpath1 in sorted(xpaths1, cmp=self._rankXpaths):
                for xpath2 in flatten([xpaths for xpaths in xpathsGroup if xpaths != xpaths1]):
                    if len(xpath1) == len(xpath2):
                        diff = xpath1.diff(xpath2)
                        if len(diff) == 1:
                            partition = diff[0]
                            # use common element if possible
                            tag = xpath1.tags()[partition]
                            if tag == xpath2.tags()[partition]:
                                abstractXpath = xpath1.copy()
                                abstractXpath[partition] = tag
                                abstractXpaths[(abstractXpath, partition)] += 1

        # sort abstract xpaths by usefulness
        return sorted(abstractXpaths.keys(), cmp=lambda a,b: self._rankAbstractions((a, abstractXpaths[a]), (b, abstractXpaths[b])))

    def _rankXpaths(self, xpath1, xpath2):
        """Rank xpath importance first on xpath length, then on alphabetically"""
        if len(xpath1.get()) != len(xpath2.get()):
            return len(xpath2.get()) - len(xpath1.get())
        else:
            return -1 if xpath1.get() < xpath2.get() else 1

    def _rankAbstractions(self, ((xpath1, partition1), count1), ((xpath2, partition2), count2)):
        """Rank xpaths first on count, then on xpath length, and finally alphabetically"""
        if count1 != count2:
            return count2 - count1
        elif len(xpath1.get()) != len(xpath2.get()):
            return len(xpath2.get()) - len(xpath1.get())
        else:
            return -1 if xpath1.get() < xpath2.get() else 1




    """def removeStatic(self):
        ""Remove content that is static and so appears across all documents""
        if len(docs) > 1:
            for text, xpaths in docs[0].getXpaths().items():
                if all((text, xpaths) in doc.getXpaths().items() for doc in docs):
                    for doc in docs:
                        doc.getXpaths().pop(text)
    """
