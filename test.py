import sys
import os
import string
import re

from sitescraper import sitescraper
from sitescraper.HtmlXpath import HtmlXpath
import testdata

#_______________________________________________________________________________

def regressionTests():
    """Run sitescraper against regression tests to ensure model generation not broken by changes"""
    ss = sitescraper(debug=True)
    for module in testdata.__all__:
        website = getattr(testdata, module)
        for url, output in website.data:
            ss.add(open('testdata/%s/%s' % (module, url)).read(), output)
        print '\n' + str(module)
        ss.train()

        # normalize xpath by extracting tag types
        normalizeModel = lambda model: sorted([([t for t in HtmlXpath(xpathStr).tags() if t != 'tbody'], flag) for (xpathStr, flag) in [(xpathStr if type(xpathStr) == tuple else (xpathStr, 0)) for xpathStr in model]])
        if normalizeModel(website.model) != normalizeModel(ss.model()):
            # expected xpath did not match so test failed
            modelStr = lambda model: '\n'.join([str(s) for s in model])
            print 'Expected:'
            print modelStr(normalizeModel(website.model))
            print modelStr(website.model)
            print 'Get:'
            print modelStr(normalizeModel(ss.model()))
            print modelStr(ss.model())
            break
        else:
            # test passed
            print 'Passed'
            #print ss.scrape('testdata/%s/%s' % (module, website.data[0][0]))
        ss.clear()
#_______________________________________________________________________________

def docTests():
    """run sitescraper doctests"""
    import os
    import sys 
    import unittest
    import doctest
    # change to code directory
    # XXX how can I do this properly by importing the module?
    os.chdir('sitescraper')
    if '.' not in sys.path: sys.path.append('.')

    suite = unittest.TestSuite()
    for mod in ['common', 'HtmlAttributes', 'HtmlDoc', 'HtmlModel', 'HtmlXpath']:
        suite.addTest(doctest.DocTestSuite(mod))
    runner = unittest.TextTestRunner()
    runner.run(suite)
#_______________________________________________________________________________

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser('usage: %prog --doc|--regression')
    parser.add_option("-d", "--doc", dest="doc", action="store_true", default=False, help="Run doctests")
    parser.add_option("-r", "--regression", dest="regression", action="store_true", help="Get regression tests")
    options, args = parser.parse_args()
    
    if options.doc:
        docTests()
    elif options.regression:
        regressionTests()
    else:
        parser.print_help()
#_______________________________________________________________________________
