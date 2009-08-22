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
    for module in testdata.__all__:
        ss = sitescraper(debug=False)
        website = getattr(testdata, module)
        for url, output in website.data:
            filename = 'testdata/%s/%s' % (module, url)
            ss.add(filename, output)
        print '\n' + str(module)
        ss.train()

        our_scrape = sorted(ss.scrape(filename))
        expected_scrape = sorted(sitescraper(model=website.model).scrape(filename))
        if all(our_scrape) and our_scrape == expected_scrape:
            # test passed
            print 'Passed'
        else:
            # expected xpath did not match so test failed
            print 'Expected:'
            print expected_scrape
            print 'Scraped:'
            print our_scrape
            print 'Expected:'
            printModel(website.model)
            print 'Scraped:'
            printModel(ss.model())
#_______________________________________________________________________________

def printModel(model):
    """Print the model in a readable form for debugging"""
    padding = ' '
    print padding, 'Raw model:'
    print padding*2, '\n'.join(str(m) for m in model)
    print padding, 'Tags:'
    for xpathStr in sorted(model):
        print padding*2, HtmlXpath(xpathStr).tags()
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
