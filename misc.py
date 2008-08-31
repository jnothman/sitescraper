from __future__ import division
import sys
import os
import re

# XXX couldn't get relative imports working so adjust the path
currentDir = os.path.abspath(os.path.dirname(__file__))
if currentDir not in sys.path:
    sys.path.insert(0, currentDir)
parentDir = os.path.join(currentDir, os.path.pardir)
if parentDir not in sys.path:
    sys.path.insert(0, parentDir)



def sortDict(d):
    """Sort dictionary keys by their values

    >>> sortDict({"Richard": 23, "Andrew": 21, "James": 15})
    ['James', 'Andrew', 'Richard']
    """
    e = d.keys()
    e.sort(cmp=lambda a,b: cmp(d[a],d[b]))
    return e


def difference(l1, l2):
    """Return indices in list that differ

    >>> difference([1,2,2,4], [1,2,3,4])
    [2]
    """
    indices = []
    for i, (v1, v2) in enumerate(zip(l1, l2)):
        if v1 != v2:
            indices.append(i)
    return indices

def unique(l):
    """Return unique elements of list

    >>> unique([1, 2, 3, 2, 2, 4])
    [1, 2, 3, 4]
    """
    seen = {}
    result = []
    for item in l:
        if item in seen: continue
        seen[item] = 1
        result.append(item)
    return result


def average(l):
    """The list average value

    >>> average([1, 2, 3, 4, 0])
    2.0
    """
    return sum(l) / len(l)


def flatten(l):
    """Expand all sublists into a single list

    >>> flatten([1, [2, 3, 4], 5])
    [1, 2, 3, 4, 5]
    """
    if isinstance(l,list):
        return sum(map(flatten, l),[])
    else:
        return [l]


def extractInt(s):
    """Extract integer from string

    >>> extractInt('hello 99!')
    99
    """
    return int(''.join(c for c in s if c in '1234567890'))


def normalizeStr(s):
    """Remove characters that make string comparison difficult from copied text"""
    return re.sub('\s+', ' ', re.sub('[\n\r]', '', s)).strip().decode('utf-8')
