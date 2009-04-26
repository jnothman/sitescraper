#
# Author: Richard Penman
# License: LGPL
# Description: 
# Interface to scraper
#

#currentDir = os.path.abspath(os.path.dirname(__file__))
#if currentDir not in sys.path:
#    sys.path.insert(0, currentDir)


from HtmlModel import HtmlModel
from HtmlDoc import HtmlDoc
from HtmlXpath import HtmlXpath



class sitescraper:
    def __init__(self, model=None, debug=False):
        self.clear()
        self._model = model
        self._debug = debug

    def clear(self):
        self._docs = []
        self._examples = []
        self._model = None

    def model(self): 
        return self._model

    def add(self, url, output):
        """Add this training data"""
        self._examples.append((url, output))

    def scrape(self, url, html=False):
        """Scrape data from this url using model from current training data
        The html flag determines whether to extract text or the raw HTML"""
        if self._examples:
            self.train() # new examples to train
        if not self._model:
            raise SiteScraperError('Error: can not scrape because model is not trained')

        doc = HtmlDoc(url, output=[], xpaths=True)
        if doc.tree().getroot() is None:
            raise SiteScraperError('Error: %s has no root node' % input)
        
        results = []
        for record in self._model:
            if type(record) == str:
                xpathStr = record
                mode = HtmlXpath.DEFAULT_MODE
            elif type(record) == tuple:
                xpathStr, mode = record
            else:
                raise SiteScraperError('Invalid model %s' % str(record))

            # extract data for this xpath
            output = doc.getElementsHTML if html else doc.getElementsText
            for result in [output(doc.tree().xpath(xpathStr))]:
                if result:
                    if mode == HtmlXpath.COLLAPSE_MODE:
                        results.append(''.join(result))
                    else:
                        results.extend(result)
                else:
                    results.append(None)
        return results

    def train(self):
        """Train model from given examples"""
        for url, output in self._examples:
            self._docs.append(HtmlDoc(url, output=output))
        self._examples = []
        # train the model
        self._model = HtmlModel(self._docs, debug=self._debug).get()



class SiteScraperError(Exception):
    pass