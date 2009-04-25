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


def trainModel(examples, debug=False):
    """Scrape html example to generate model"""
    model = HtmlModel(examples, debug)
    return model.get()


def applyModel(model, input):
    """Use the model to extract output for a url of the same form"""
    doc = HtmlDoc(input, xpaths=True)
    if doc.getTree().getroot() is None:
        print 'Error: %s has no root node' % input
        return []
    
    results = []
    for record in model:
        if type(record) == tuple:
            xpathStr, mode = record
        elif type(record) == str:
            xpathStr = record
            mode = HtmlXpath.DEFAULT_MODE
        else:
            raise Exception('Invalid model %s' % str(record))

        thisResults = [doc.getElementsHTML(doc.getTree().xpath(xpathStr))]
        for thisResult in thisResults:
            if thisResult:
                if mode == HtmlXpath.COLLAPSE_MODE:
                    results.append(''.join(thisResult))
                else:
                    results.extend(thisResult)
            else:
                results.append(None)

    return results
