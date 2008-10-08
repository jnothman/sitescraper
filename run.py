import sys
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))
import re
import doctest
import unittest
from difflib import SequenceMatcher
from misc import normalizeStr, average, pretty, buildUrlRE, commonStart, anyIn
import __init__ as sitescraper
from data import *


def getData(data):
    os.chdir('data')
    #googleModel = sitescraper.trainModel([
    #('http://www.google.com.au/search?num=100&q=site:unimelb.edu.au', ['www.unimelb.edu.au/', 'www.unimelb.edu.au/accessibility/']),
    #('http://www.google.com.au/search?num=100&q=site:google.com', ['video.google.com/', 'adwords.google.com/']),
    #])
    googleModel = sitescraper.trainModel([
        ('file:html/search/google/1.html', ['www.holden.com.au/ - 2k', 'www.holden.com.au/www-holden/ - 14k']),
        ('file:html/search/google/2.html', ['www.ford.com.au/ - 34k', 'www.ford.com/ - 32k']),
    ])
    
    maxUrls = 150
    maxPages = 50
    for site, d in data:
        print site
        #if site != 'ASX': continue
        trainUrls = [url.replace('file:', '') for (url, outputs) in d]
        #print 'RE:', buildUrlRE(trainUrls)
        baseDir = '%s' % os.path.dirname(trainUrls[0])
        searchStrs = [s for s in open('%s/url.txt' % baseDir).read().split('\n') if s]

        urls = []
        if len(searchStrs) == 1:
            # have been given a regular expression to expand
            searchStr = searchStrs[0]
            if anyIn(['search', 'stocks', 'commerce'], baseDir):
                # this category has a special search defined
                for i, term in enumerate(open('%s/../popular.txt' % baseDir).readlines()[:maxUrls]):
                    url = searchStr % term
                    urls.append(url.replace('\n', ''))
            else:
                baseUrl = searchStr[:searchStr.index('%s')]
                pageSize = 100
                for pageNo in range(maxPages):
                    googleUrl = 'http://www.google.com.au/search?num=%d&start=%d&q=site:%s' % (pageSize, pageNo*pageSize, baseUrl)
                    result = sitescraper.testModel(googleUrl, googleModel)
                    if result:
                        googleUrls = [url.split()[0] for url in result]
                        regExpStr = re.escape(searchStr.replace('http://', '').strip()).replace('\\%s', '[^/]+') + '$'
                        #print searchStr, regExpStr
                        regExp = re.compile(regExpStr)
                        urls.extend([url for url in googleUrls if regExp.search(url)])
                        #print pageNo, len(urls)
                    if not result or len(urls) > 3*maxUrls:
                        # no more results
                        break
        else:
            # have been given a set of urls, which can use directly
            urls = searchStrs

        print len(urls)
        testDir = '%s/test' % baseDir
        if not os.path.exists(testDir):
            os.makedirs(testDir)
        for i, url in enumerate(urls):
            #if i <= 100: continue
            os.system("""wget "%s" --user-agent="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a9pre) Gecko/2007100205 Minefield/3.0a9pre" -O %s/%d.html""" % (url, testDir, i+1))


# change to fold testing
def testData(data):
    DEBUG = 0
    FUZZY = 0
    modelSize = 3
    os.chdir('data')
    accuracies = []
    doc = sitescraper.htmlDoc('', True, True)
    S = 0
    for site, d in data[S:S+1]:
        siteAccuracies = []
        model = sitescraper.trainModel(d[:modelSize])
        print site, 'model:'
        print pretty(model)
        for url, expectedOutput in d:
            generatedOutput = sitescraper.testModel(url, model)
            print url
            if DEBUG:
                print 'GET:'
                for o in generatedOutput:
                    print o.replace('\n', '') + '\n'
                print
                print 'EXPECT:'
                for o in expectedOutput:
                    print o.replace('\n', '') + '\n'
            for i, e in enumerate(expectedOutput):
                e = normalizeStr(e)
                bestScore = doc.similarity(e, '')
                if e:
                    scores = []
                    for g in generatedOutput:
                        g = normalizeStr(g)
                        scores.append(((bestScore - doc.similarity(e, g))/2, g))
                    if scores:
                        score, g = max(scores)
                    else:
                        score, g = 0, ''
                    accuracy = max(0, 100 * score / float(bestScore))
                    if accuracy < 95:
                        print '%d/%d (%.2f%%)' % (score, bestScore, accuracy)
                        #print doc.sequence.get_opcodes()
                        print 'Expected:', e
                        print 'Get:     ', g
                        print
                        if FUZZY:
                            siteAccuracies.append(accuracy)
                        else:
                            siteAccuracies.append(0)
                    else:
                        # consider fully accurate when this close
                        # generally the difference is due to changes in text when copying and pasting
                        siteAccuracies.append(100)
        accuracies.append((site, average(siteAccuracies)))
    print ['%s: %.2f%%' % (site, a) for (site, a) in accuracies]
    print 'Accuracy: %.2f%%' % average([a for (site, a) in accuracies])


def docTests():
    suite = unittest.TestSuite()
    for mod in ['__init__', 'misc']:
        suite.addTest(doctest.DocTestSuite(__import__(mod)))
    runner = unittest.TextTestRunner()
    runner.run(suite)



if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser('usage: %prog --doc|--get=<data>|--test=<data>')
    parser.add_option("-d", "--doc", dest="doc", action="store_true", default=False, help="Run doctests")
    parser.add_option("-g", "--get", dest="get", action="store", help="Get url data")
    parser.add_option("-t", "--test", dest="test", action="store", help="Run sitescraper over this test data")
    options, args = parser.parse_args()
    
    fn = None
    if options.doc:
        docTests()
    elif options.get:
        fn, file = getData, options.get
    elif options.test:
        fn, file = testData, options.test
    else:
        parser.print_help()

    if fn:
        import data
        fn(getattr(data, file).data)
