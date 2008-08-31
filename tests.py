import sys
import os
import doctest
import unittest
sys.path.append('..')
import sitescraper as ss
import misc
from data import *


def runExampleData():
    modelSize = 3
    os.chdir('data')
    for site, d in sorted(data.items()):
        model = ss.trainModel(d[:modelSize])
        print site, 'model:', model
        for url, expectedOutput in d:#[modelSize:]:
            generatedOutput = ss.testModel(url, model)
            #print "Expected:", expectedOutput
            #print "Get:", generatedOutput
            """for i, e in enumerate(expectedOutput):
                try:
                    g = generatedOutput[i]
                except IndexError:
                    g = ''
                print '%d/%d' % (lcs_len(e, g), len(normalize_str(e))),"""
            print
            for e in expectedOutput:
                for g in generatedOutput:
                    print '%d/%d' % (misc.lcs_len(e, g), len(misc.normalize_str(e))),
                print
            #print expectedOutput
            #print
            #print generatedOutput
        break


def runDocTests():
    suite = unittest.TestSuite()
    for mod in ['__init__', 'misc']:
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
