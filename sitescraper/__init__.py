from HtmlModel import HtmlModel
from HtmlDoc import HtmlDoc
from HtmlXpath import HtmlXpath



class sitescraper:
    """The interface to SiteScraper"""
    #___________________________________________________________________________

    def __init__(self, model=None, debug=False):
        self.clear()
        self._model = model
        self._debug = debug
    #___________________________________________________________________________

    def __len__(self):
        return len(self._examples)
    #___________________________________________________________________________

    def clear(self):
        self._docs = []
        self._previousInput = None
        self._previousDoc = None
        self._examples = []
        self._model = None
    #___________________________________________________________________________
    
    def model(self): 
        if self._examples:
            self.train() # new examples to train
        return self._model
    #___________________________________________________________________________
    
    def add(self, input, outputs):
        """Add this training data"""
        self._examples.append((input, outputs))
    #___________________________________________________________________________

    def scrape(self, input, html=False):
        """Scrape data from this input using model from current training data
        The html flag determines whether to extract the raw HTML instead of parsed text"""
        if not self.model():
            raise SiteScraperError('Error: can not scrape because model is not trained')

        if self._previousInput != input:
            self._previousInput = input
            self._previousDoc = HtmlDoc(input, outputs=[], xpaths=[])
        doc = self._previousDoc
        if doc.tree().getroot() is None:
            raise SiteScraperError('Error: %s has no root node' % input)
        
        outputFn = doc.getElementHTML if html else doc.getElementText
        results = []
        for xpathStr in self._model:
            isGroup = isinstance(xpathStr, list)
            if isGroup:
                xpathStr = xpathStr[0]
            result = [(e if isinstance(e, str) else outputFn(e)) for e in doc.tree().xpath(xpathStr)]
            if isGroup:
                results.append(result)
            else:
                if result:
                    results.append(' '.join(result))
                else:
                    results.append(None) # distinguish empty match from no match
        return results
    #___________________________________________________________________________

    def train(self):
        """Train model from given examples"""
        for input, outputs in self._examples:
            self._docs.append(HtmlDoc(input, outputs=outputs))
        self._examples = []
        # train the model
        self._model = HtmlModel(self._docs, debug=self._debug).get()
    #___________________________________________________________________________



class SiteScraperError(Exception):
    pass
