from collections import defaultdict
from HtmlDoc import HtmlDoc
from HtmlXpath import HtmlXpath
from HtmlAttributes import HtmlAttributes
from common import normalizeStr, unique, pretty, flatten, extractInt



class HtmlModel:
    """Generates a model to extract the desired information in a webpage
    """

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
    #___________________________________________________________________________

    def get(self):
        """Get a string list representation of the model
        """
        if self._model is None:
            # need to generate model
            self._model = [xpath.get() for xpath in self.trainModel()]
        return self._model
    #___________________________________________________________________________

    def trainModel(self):
        """Train the model using the known output for the given urls
        """
        # rate xpaths by the similarity of their content with the output
        modelXpaths = []
        moreData = True
        i = 0
        while moreData:
            isGroup = False
            xpaths = []
            for doc in self._docs:
                if i < len(doc.outputs()):
                    outputs = doc.outputs()[i]
                    if isinstance(outputs, list):
                        isGroup = True
                    else:
                        outputs = [outputs]
                    for output in outputs:
                        outputScores = defaultdict(int)
                        for xpath, score in doc.matchXpaths(normalizeStr(output)):
                            outputScores[xpath] += score

                        # select best xpath match for each output
                        bestScore = min([score for (xpath, score) in outputScores.items()])
                        if bestScore > 0: 
                            print "Warning: could not find '%s' (score=%d)" % (output, score)
                        xpaths.extend([xpath for (xpath, score) in outputScores.items() if score == bestScore])
                        #xpaths.append(min([(score, xpath) for (xpath, score) in outputScores.items()])[1])
            if xpaths:
                if isGroup:
                    modelXpaths.append(self.abstractXpaths(xpaths))
                else:
                    modelXpaths.append(sorted(xpaths, cmp=self._rankXpaths)[0])
                i += 1
            else:
                moreData = False # reached the end of expected output data

            """if self._debug:
                for i, xpaths in enumerate(modelXpaths):
                    print [doc.outputs()[i] for doc in self._docs if len(doc) > i][0].replace('\n', '')
                    print pretty(xpaths)"""
        if self._attributes:
            modelXpaths = self.addAttributes(modelXpaths)
        return modelXpaths
    #___________________________________________________________________________

    def addAttributes(self, xpaths):
        """Replace xpath indices with attributes where possible
        """
        A = HtmlAttributes(self._docs)
        xpathAttribs = []
        for xpath in xpaths:
            xpathAttribs.append(A.addAttribs(xpath.copy(), A.uniqueAttribs(xpath)))
        return xpathAttribs
    #___________________________________________________________________________

    def abstractXpaths(self, xpaths):
        """Find a single xpath to represent this group of xpaths by replacing similar xpaths with a regular expression

        >>> doc = HtmlDoc('../testdata/yahoo_search/1.html', [])
        >>> xpathsGroup = [\
            [HtmlXpath('/html[1]/body[1]/table[1]/tr[1]/td[1]'), HtmlXpath('/html[1]/body[1]/table[1]/tr[1]')],\
            [HtmlXpath('/html[1]/body[1]/table[1]/tr[2]/td[1]'), HtmlXpath('/html[1]/body[1]/table[1]/tr[2]')],\
            [HtmlXpath('/html[1]/body[1]/table[1]/tr[3]'),],\
            [HtmlXpath('/html[1]/body[1]/a[1]')],\
        ]
        >>> [xpath.get() for xpath in HtmlModel([doc]).refineXpaths(xpathsGroup)]
        ['/html[1]/body[1]/a[1]', '/html[1]/body[1]/table[1]/tr']
        """
        popularity = defaultdict(list)
        for xpath1 in xpaths:
            for xpath2 in xpaths:
                if len(xpath1) == len(xpath2) and xpath1 != xpath2:
                    diff = xpath1.diff(xpath2)
                    abstractXpath = HtmlXpath([str(xpath1)])
                    indices = []
                    for partition in diff:
                        tag = xpath1.tags()[partition]
                        if tag != xpath2.tags()[partition]:
                            tag = '*' # have different tags
                        abstractXpath[partition] = tag
                        indices.append(extractInt(xpath1[partition]))
                    popularity[(abstractXpath, diff)].append(indices)
                    #if self._debug:
                    #    print 'Abstracted: %s' % abstractXpath

        # find the most popular regular expression
        abstractXpath, diff = sorted([(len(v), k) for (k, v) in popularity.items()])[-1][1]
        # restrict xpath regular expressions to lowest index encountered
        minIndices = [min(indices) for indices in zip(*popularity[(abstractXpath, diff)])]
        for partition, minIndex in zip(diff, minIndices):
            #minIndex = min([indices[i] for indices in popularity[(abstractXpath, diff)]])
            #minIndex = min(indices)
            if minIndex > 1:
                abstractXpath[partition] += '[position()>%d]' % (minIndex - 1)
        return abstractXpath
    #___________________________________________________________________________
    
    def _rankXpaths(self, xpath1, xpath2):
        """Rank xpath importance first on xpath length, then on alphabetically
        """
        if len(str(xpath1)) != len(str(xpath2)):
            return len(str(xpath2)) - len(str(xpath1))
        else:
            return -1 if str(xpath1) < str(xpath2) else 1
