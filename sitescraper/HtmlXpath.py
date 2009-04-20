import re
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
    sepRE = re.compile('/+')

    def __init__(self, xpathStr):
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

    def __eq__(self, other):
        return self.get() == other.get()

    def copy(self):
        return HtmlXpath(self.get())

    def get(self): 
        return self._xpathStr

    def set(self, xpathStr): 
        self._xpathStr = xpathStr
        return self

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
        if anyIn(['*', '//'], self.get()):
            return False
        else:
            return self.copy().normalize() == self

    def isAllContent(self):
        """xpaths with '//' as a separator will return all sub nodes

        >>> HtmlXpath('/a[1]/b/c').isAllContent()
        False
        >>> HtmlXpath('/a[1]/b//c').isAllContent()
        True
        """
        return '//' in self.get()

    def diff(self, other):
        """Returns indices where xpaths differ. Return all indices if are different length.

        >>> HtmlXpath('/a/c/c').diff(HtmlXpath('/a/b/c'))
        [1]
        >>> HtmlXpath('/a/b/c').diff(HtmlXpath('/a/b/c/d/e'))
        [0, 1, 2]
        """
        indices = []
        if self != other:
            force = self.isAllContent() != other.isAllContent() or len(self) != len(other)
            for i, (v1, v2) in enumerate(zip(self, other)):
                if force or v1 != v2:
                    indices.append(i)
            #indices.extend(range(i+1, max(len(self), len(other))))
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
        xpathREstrs = {}
        for xpath1 in xpaths:
            for xpath2 in xpaths:
                if xpath1 != xpath2:
                    diff = xpath1.diff(xpath2)
                    if len(diff) == 1:
                        partition = diff[0]
                        # use common element if possible, else '*' to match any
                        x1pathTag = xpath1.tags()[partition]
                        if x1pathTag == xpath2.tags()[partition]:
                            abstraction = x1pathTag
                            #else:
                            #    abstraction = '*'
                            xpathRE = xpath1.copy()
                            xpathRE[partition] = abstraction
                            xpathREstr = xpathRE.get()
                            xpathREstrs.setdefault((xpathREstr, partition), 0)
                            xpathREstrs[(xpathREstr, partition)] += 1
        return xpathREstrs
    abstractSet = staticmethod(abstractSet)
