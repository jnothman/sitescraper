import sys
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))
import doctest
import unittest
from difflib import SequenceMatcher
from misc import normalizeStr
import sitescraper as ss
from data import *


# change to fold testing
def runExampleData():
    modelSize = 3
    os.chdir('data')
    for site, d in sorted(data.items()):
        model = ss.trainModel(d[:modelSize])
        print site, 'model:', model
        for url, expectedOutput in d:
            print url
            generatedOutput = ss.testModel(url, model)
            for i, e in enumerate(expectedOutput):
                e = normalizeStr(e)
                if i < len(generatedOutput):
                    g = normalizeStr(generatedOutput[i])
                else:
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
                    pass # success!



def runDocTests():
    suite = unittest.TestSuite()
    for mod in ['sitescraper', 'misc']:
        suite.addTest(doctest.DocTestSuite(__import__(mod)))
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
