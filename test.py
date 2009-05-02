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
    ss = sitescraper(debug=False, html=True)
    for module in testdata.__all__:
        website = getattr(testdata, module)
        for url, output in website.data:
            ss.add(open('testdata/%s/%s' % (module, url)).read(), output)
        print '\n' + str(module)
        ss.train()

        url = website.data[0][0]
        if ss.scrape(url) == sitescraper(model=website.model, html=True).scrape(url):
            # test passed
            print 'Passed'
        else:
            # expected xpath did not match so test failed
            print 'Expected:'
            printModel(website.model)
            print 'Scraped:'
            printModel(ss.model())
        ss.clear()
#_______________________________________________________________________________

def printModel(model):
    """Print the model in a readable form for debugging"""
    padding = ' '
    print padding, 'Raw model:'
    print padding*2, '\n'.join(str(m) for m in model)
    print padding, 'Tags:'
    for xpathStr in sorted(model):
        if type(xpathStr) == tuple:
            xpathStr, mode = xpathStr
        else:
            mode = 0
        print padding*2, HtmlXpath(xpathStr).tags(), mode
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
