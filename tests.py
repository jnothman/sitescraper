import sys
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))
import doctest
import unittest
from difflib import SequenceMatcher
from misc import normalizeStr, average
import __init__ as sitescraper
from data import *


# change to fold testing
def runExampleData():
    modelSize = 3
    os.chdir('data')
    accuracies = []
    X = sitescraper.xmlXpaths('', True, True)
    i = 4
    for site, d in data[i:i+1]:
        siteAccuracies = []
        model = sitescraper.trainModel(d[:modelSize])
        print site, 'model:', model
        for url, expectedOutput in d:
            print url
            generatedOutput = sitescraper.testModel(url, model)
            #print 'G: ' + '\n'.join(generatedOutput)
            #print
            #print 'E: ' + '\n'.join(expectedOutput)
            #sys.exit()
            for i, e in enumerate(expectedOutput):
                e = normalizeStr(e)
                bestScore = X.similarity(e, '')
                if e:
                    scores = []
                    for g in generatedOutput:
                        g = normalizeStr(g)
                        scores.append((bestScore - X.similarity(e, g), g))
                    if scores:
                        score, g = max(scores)
                    else:
                        score, g = 0, ''
                    accuracy = 100 * score / float(2*bestScore)
                    siteAccuracies.append(accuracy)
                    if accuracy < 99:
                        print '%d/%d (%d%%)' % (score, 2*bestScore, accuracy)
                        print X.sequence.get_opcodes()
                        print 'Expected:', e
                        print 'Get:     ', g
                        print
        accuracies.append(siteAccuracies)
    print ['%.2f%%' % average(a) for a in accuracies]
    print 'Accuracy: %.2f%%' % average([average(a) for a in accuracies])


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
