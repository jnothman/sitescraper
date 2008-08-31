import re


def commonStart(ss):
    """Takes a list of strings and returns first index where strings differ

    >>> commonStart(['happy birthday', 'happy holiday'])
    6
    """
    try:
        first_s = ss[0]
        for i, ch in enumerate(first_s):
            for s in ss:
                if ch != s[i]:
                    raise IndexError
    except IndexError:
        pass # mismatch so finish loop and return current index

    return i

# reverse a string efficiently
strReverse = lambda s: ''.join([s[-1 - i] for i in xrange(len(s))])


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


def flatten(l):
    """Expand all sublists into a single list

    >>> flatten([1, [2, 3, 4], 5])
    [1, 2, 3, 4, 5]
    """
    if isinstance(l,list):
        return sum(map(flatten, l),[])
    else:
        return [l]


def normalize_str(s):
    """Remove characters that make string comparison difficult"""
    return re.sub('[\n\r ]', '', s)


def lcs_len(a, b):
    """Return the longest common substring shared by both the 2 strings"""
    a = normalize_str(a)
    b = normalize_str(b)
    L = [[0] * (len(b)+1) for i in xrange(len(a)+1)]
    lcs = 0
    for i in xrange(len(a)):
        for j in xrange(len(b)):
            if a[i] == b[j]:
                L[i+1][j+1] = L[i][j] + 1
                lcs = max(lcs, L[i+1][j+1])
    return lcs
