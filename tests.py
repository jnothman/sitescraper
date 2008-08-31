import sys
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))
import doctest
import unittest
from difflib import SequenceMatcher
import misc
import sitescraper as ss
from data import *


def runExampleData():
    modelSize = 3
    os.chdir('data')
    for site, d in sorted(data.items()):
        model = ss.trainModel(d[:modelSize])
        print site, 'model:', model
        for url, expectedOutput in d:#[modelSize:]:
            print url
            generatedOutput = ss.testModel(url, model)
            for i, e in enumerate(expectedOutput):
                e = misc.normalizeStr(e)
                try:
                    g = misc.normalizeStr(generatedOutput[i])
                except IndexError:
                    g = ''

                s = SequenceMatcher(None, e, g)
                thisLCS = sum(n for (i, j, n) in s.get_matching_blocks())
                maxLCS = len(e)
                if thisLCS < 0.99*maxLCS:
                    print '%d/%d (%d%%)' % (thisLCS, maxLCS, 100 * thisLCS // maxLCS)
                    print 'Expected:'
                    print e
                    print
                    print 'Get:'
                    print g
                    print
                    print
                else:
                    # success!
                    pass
            """for e in expectedOutput:
                for g in generatedOutput:
                    print '%d/%d' % (misc.lcs_len(e, g), len(misc.normalizeStr(e))),
                print
            """



def runDocTests():
    suite = unittest.TestSuite()
    for mod in [ss, misc]:
        suite.addTest(doctest.DocTestSuite(mod))
    runner = unittest.TextTestRunner()
    runner.run(suite)



if __name__ == '__main__':
    args = sys.argv[1:]
    if 'data' in args:
        runExampleData()
    elif 'doc' in args:
        runDocTests()
    else:
        print('Usage: python %s data|doc' % sys.argv[0])
