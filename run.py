import sys
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))
import doctest
import unittest
from difflib import SequenceMatcher
from misc import normalizeStr, average, pretty
import __init__ as sitescraper
from data import *

DEBUG = 0


# change to fold testing
def runExampleData(data):
    modelSize = 3
    os.chdir('data')
    accuracies = []
    doc = sitescraper.htmlDoc('', True, True)
    i = 6
    for site, d in data:#[i:i+1]
        siteAccuracies = []
        model = sitescraper.trainModel(d[:modelSize])
        print site, 'model:'
        print pretty(model)
        for url, expectedOutput in d:
            generatedOutput = sitescraper.testModel(url, model)
            print url
            if DEBUG:
                print 'G: ' + pretty(generatedOutput)
                print
                print 'E: ' + pretty(expectedOutput)
                sys.exit()
            for i, e in enumerate(expectedOutput):
                e = normalizeStr(e)
                bestScore = doc.similarity(e, '')
                if e:
                    scores = []
                    for g in generatedOutput:
                        g = normalizeStr(g)
                        scores.append((bestScore - doc.similarity(e, g), g))
                    if scores:
                        score, g = max(scores)
                    else:
                        score, g = 0, ''
                    accuracy = max(0, 100 * score / float(2*bestScore))
                    if accuracy < 95:
                        print '%d/%d (%d%%)' % (score, 2*bestScore, accuracy)
                        #print doc.sequence.get_opcodes()
                        print 'Expected:', e
                        print 'Get:     ', g
                        print
                        siteAccuracies.append(accuracy)
                    else:
                        # consider fully accurate when this close
                        # generally the difference is due to changes in text when copying and pasting
                        siteAccuracies.append(100)
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
    if not args:
        print('Usage: python %s data|doc' % sys.argv[0])
    elif 'doc' in args:
        runDocTests()
    else:
        import data
        runExampleData(getattr(data, args[0]).data)
