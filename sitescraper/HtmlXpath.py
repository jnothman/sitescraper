import re
from collections import defaultdict
from misc import anyIn



class HtmlXpath(object):
    """Encapsulate an xpath

    >>> x = HtmlXpath('/html/body//a')
    >>> x[1]
    'body'
    >>> x[2] = 'p[1]'
    >>> x.get()
    '/html/body//p[1]'
    >>> list(x)
    ['html', 'body', 'p[1]']
    """
    MODES = DEFAULT, COLLAPSE = 0, 1
    sepRE = re.compile('/+')

    def __init__(self, xpathStr, mode=DEFAULT):
        self._mode = mode
        self.set(xpathStr)

    def __len__(self):
        return len(self.sections())

    def __getitem__(self, i):
        return self.sections()[i]
    def __setitem__(self, i, v):
        xpath = self.get()
        starts, ends = [], []
        for j, match in enumerate(re.finditer(HtmlXpath.sepRE, xpath)):
            starts.append(match.end())
            if match.start() > 0:
                ends.append(match.start())
            if j > i: 
                break
        ends.append(len(xpath))
        self.set(xpath[:starts[i]] + v + xpath[ends[i]:])
        return self

    def __iter__(self):
        return self.sections().__iter__()

    def __str__(self):
        return self.get()

    def __cmp__(self, other):
        return cmp(self.get(), other.get())

    def __hash__(self):
        return hash(self.get())

    def copy(self):
        return HtmlXpath(self.get(), self.mode())

    def get(self): 
        return self._xpathStr

    def set(self, xpathStr): 
        self._xpathStr = xpathStr
        return self

    def mode(self):
        return self._mode

    def sections(self):
        """Return sections of xpath

        >>> HtmlXpath('/a/b/c').sections()
        ['a', 'b', 'c']
        >>> HtmlXpath('/a[1]/b').sections()
        ['a[1]', 'b']
        >>> HtmlXpath('/a/b//c').sections()
        ['a', 'b', 'c']
        """
        return re.split(HtmlXpath.sepRE, self.get())[1:]

    def tags(self):
        """Return list of tags in xpath
        
        >>> HtmlXpath('/a/b[1]//c').tags()
        ['a', 'b', 'c']
        """
        removeIndex = lambda s: '[' in s and s[:s.index('[')] or s
        return [removeIndex(s) for s in self.sections()]

    def walk(self):
        """Return list of sub xpaths

        >>> HtmlXpath('/a/b/c').walk()
        ['/a', '/a/b', '/a/b/c']
        >>> HtmlXpath('/a[1]/b').walk()
        ['/a[1]', '/a[1]/b']
        >>> HtmlXpath('/a/b//c').walk()
        ['/a', '/a/b', '/a/b//c']
        """
        xpaths = []
        for match in re.finditer(HtmlXpath.sepRE, self.get()):
            end = match.start()
            if end > 0:
                xpaths.append(self.get()[:end])
        xpaths.append(self.get())
        return xpaths


    def normalize(self):
        """A normalized xpath has an index defined at each node. ElementTree treats indexless nodes as a regular expression.
        
        >>> HtmlXpath("/a[1]/b/c[@id='2']/d").normalize().get()
        "/a[1]/b[1]/c[@id='2']/d[1]"
        """
        for i, section in enumerate(self):
            if section != '*' and not section.endswith(']'):
                self[i] = section + '[1]'
        return self

    def isNormalized(self):
        """
        >>> HtmlXpath('/a[1]/b[2]').isNormalized()
        True
        >>> HtmlXpath('/a[1]/b').isNormalized()
        False
        >>> HtmlXpath('/a[1]//b[2]').isNormalized()
        False
        """
        return self.copy().normalize() == self

    def diff(self, other):
        """Returns indices where xpaths differ.

        >>> HtmlXpath('/a/c/c').diff(HtmlXpath('/a/b/c'))
        [1]
        >>> HtmlXpath('/a/b/c').diff(HtmlXpath('/a/b/c/d/e'))
        [3, 4]
        """
        indices = []
        if self != other:
            for i in range(max(len(self), len(other))):
                if i >= len(self) or i >= len(other) or self[i] != other[i]:
                    indices.append(i)
        return indices

    def abstractSet(xpaths):
        """Abstract set of xpaths with regular expressions
        Return a dictionary with each abstracted xpath and the number of original xpaths that match
        
        >>> xpaths = []
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/p[1]/span[1]/p[1]/strong[1]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[1]/h3[1]/a[1]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/div[1]/h3[1]/a[1]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/div[1]/h3[1]/a[1]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/div[2]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/div[2]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/div[2]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[1]/div[1]/span[1]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/span[1]'))
        >>> xpaths.append(HtmlXpath('/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/span[1]'))
        >>> [x for (x, partition) in sortDict(HtmlXpath.abstractSet(xpaths), reverse=True)[:5]]
        ['/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/span[1]', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/div[2]', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/div[1]/h3[1]/a[1]', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[2]/div[1]/*', '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li[3]/div[1]/*']
        """
        xpathREs = defaultdict(int)
        for xpath1 in xpaths:
            for xpath2 in xpaths:
                if len(xpath1) == len(xpath2):
                    diff = xpath1.diff(xpath2)
                    if len(diff) == 1:
                        partition = diff[0]
                        # use common element if possible
                        tag = xpath1.tags()[partition]
                        if tag == xpath2.tags()[partition]:
                            xpathRE = xpath1.copy()
                            xpathRE[partition] = tag
                            xpathREs[(xpathRE, partition)] += 1
        return xpathREs
    abstractSet = staticmethod(abstractSet)
