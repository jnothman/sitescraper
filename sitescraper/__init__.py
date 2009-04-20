#
# Author: Richard Penman
# License: LGPL
# Description: 
# Model the desired information in a webpage
#

#currentDir = os.path.abspath(os.path.dirname(__file__))
#if currentDir not in sys.path:
#    sys.path.insert(0, currentDir)

UNDEFINED = -1
DEBUG = 0


from HtmlDoc import HtmlDoc
from HtmlXpath import HtmlXpath
from HtmlAttributes import HtmlAttributes
from misc import normalizeStr, unique



def _rankXpaths((xpath1, score1), (xpath2, score2)):
    """Rank xpaths first on score, then on all content, then on xpath length"""
    if score1 != score2:
        return score1 - score2
    elif xpath1.isAllContent() != xpath2.isAllContent():
        return xpath1.isAllContent() and -1 or 1
    else:
        return len(xpath2.get()) - len(xpath1.get())

def trainModel(examples):
    """Train the model using the known output for the given urls

    >>> from data import training
    >>> os.chdir('data')
    >>> modelSize = 3
    >>> asx = training.data[0][1][:modelSize]
    >>> trainModel(asx)
    [("/html[1]/body[1]/div[@class='a9721']/div[@id='container']/div[@id='wrap']/div[@id='content']/div[@id='col']/table[@cellspacing='0'][@class='datatable']/tr[2]/td[@class='last']", False), ("/html[1]/body[1]/div[@class='a9721']/div[@id='container']/div[@id='wrap']/div[@id='content']/div[@id='col']/table[@cellspacing='0'][@class='datatable']/tr[2]/td[6]", False), ("/html[1]/body[1]/div[@class='a9721']/div[@id='container']/div[@id='wrap']/div[@id='content']/div[@id='col']/table[@cellspacing='0'][@class='datatable']/tr[2]/td[7]", False)]
    """
    docs = [HtmlDoc(input) for (input, _) in examples]
    #htmlDoc.removeStatic(docs)

    allOutputXpathStrs = []
    # rate xpaths by the similarity of their content with the output
    for doc, (_, outputs) in zip(docs, examples):
        for i, output in enumerate(outputs):
            if i == len(allOutputXpathStrs): allOutputXpathStrs.append({})
            for xpath, score in doc.matchXpaths(normalizeStr(output)):
                xpathStr = xpath.get()
                allOutputXpathStrs[i].setdefault(xpathStr, 0)
                allOutputXpathStrs[i][xpathStr] += score

    # select best xpath match for each output
    bestXpaths = []
    for i, outputXpathStrs in enumerate(allOutputXpathStrs):
        rankedXpaths = sorted([(HtmlXpath(xpathStr), score) for (xpathStr, score) in outputXpathStrs.items() if score < 0], _rankXpaths)
        if rankedXpaths:
            bestXpath = rankedXpaths[0][0]
            if bestXpath not in bestXpaths:
                bestXpaths.append(bestXpath)
        if DEBUG:
            print [o[i] for (_, o) in examples if len(o) > i][0].replace('\n', '')
            for xpath, score in rankedXpaths[:5]:
                print '%6d: %s' % (score, xpath)
            print
    # store xpaths that were abstracted for a single output, and so must be collapsed together
    collapsableXpaths = [xpath for xpath in bestXpaths if not xpath.isNormalized()]
    abstractedXpaths = HtmlDoc.removeRedundant(bestXpaths[:], docs)
    # replace xpath indices with attributes where possible
    A = HtmlAttributes(docs)
    attributeXpathStrs = []
    for xpath in abstractedXpaths:
        collapse = xpath in collapsableXpaths or xpath.isAllContent()
        attributeXpath = A.addAttribs(xpath.copy(), A.uniqueAttribs(xpath))
        attributeXpathStrs.append((attributeXpath.get(), collapse))

    if DEBUG:
        """for i, output in enumerate(outputs):
            print
            print output
            for xpath, score in allOutputXpathStrs[i].items()[:5]:
                if score < 0:
                    print '%6d: %s' % (score, xpath)"""
        print 'C:\n', pretty(collapsableXpaths)
        print 'best:\n', pretty(bestXpaths)
        print 'abstract:\n', pretty(abstractedXpaths)
        #print 'attribute:\n', pretty(attributeXpathStrs)
    return unique(attributeXpathStrs)


def applyModel(model, input):
    """Use the model to extract output for a url of the same form"""
    doc = HtmlDoc(input, xpaths=True)
    if doc.getTree().getroot() is None:
        print 'Error: %s has no root node' % input
        return []
    
    results = []
    for xpathStr, collapse in model:
        if '//' in xpathStr and collapse:
            # need to calculate sections separately to prevent collapsing unrelated parts
            base, ext = xpathStr.split('//')
            thisResults = [doc.getElementsHTML(e.xpath('.//' + ext)) for e in doc.getTree().xpath(base)]
        else:
            thisResults = [doc.getElementsHTML(doc.getTree().xpath(xpathStr))]
        
        for thisResult in thisResults:
            if thisResult:
                if collapse:
                    results.append(''.join(thisResult))
                else:
                    results.extend(thisResult)
            else:
                results.append('')

    return results
