import re
from collections import defaultdict
from common import flatten



class HtmlAttributes:
    """Extract attributes from XML tree and store them reverse indexed by attribute

    >>>
    >>> d1 = HtmlDoc('file:data/html/search/yahoo/1.html')
    >>> d2 = HtmlDoc('file:data/html/search/yahoo/2.html')
    >>> d3 = HtmlDoc('file:data/html/search/yahoo/3.html')
    >>> a = HtmlAttributes([d1, d2, d2])
    >>> xpath = '/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/ol[1]/li/div[1]/span[1]'
    >>> e1 = d1.getTree().xpath(xpath)[0]
    >>> a.extractAttribs(e1)
    [('class', 'url')]
    >>> attribs = a.uniqueAttribs(htmlXpath(xpath))
    >>> attribs
    [[], [], [('id', 'doc')], [('id', 'bd')], [('id', 'results')], [('id', 'left')], [('id', 'main')], [('id', 'web')], [('start', '1')], [], [('class', 'res')], [('class', 'url')]]
    >>> a.addAttribs(htmlXpath(xpath), attribs).get()
    "/html[1]/body[1]/div[@id='doc']/div[@id='bd']/div[@id='results']/div[@id='left']/div[@id='main']/div[@id='web']/ol[@start='1']/li/div[@class='res']/span[@class='url']"

    >> tree = lxmlHtml.fromstring("<html><body node='0'><c class='1' node='1'>C<d class='2'></d></c><c class='1' node='2'>D</c></body</html>").getroottree()
    >> a = HtmlAttributes(tree)
    >> extractXpaths(tree)
    {'C': ['/html[1]/body[1]/c[1]'], 'D': ['/html[1]/body[1]/c[2]']}
    >> a.extractAttribs(['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]'])
    {('node', '0'): ['/html[1]/body[1]'], ('node', '2'): ['/html[1]/body[1]/c[2]'], ('node', '1'): ['/html[1]/body[1]/c[1]'], ('class', '1'): ['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]']}
    >> attribs = a.commonAttribs(['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]'])
    >> attribs
    [('/html[1]/body[1]', ('node', '0')), ('/html[1]/body[1]/c[2]', ('class', '1'))]
    >> a.addCommonAttribs(attribs, ['/html[1]/body[1]/c[1]', '/html[1]/body[1]/c[2]'])
    ["/html[1]/body[1][@node='0']/c[1][@class='1']", "/html[1]/body[1][@node='0']/c[2][@class='1']"]
    """


    def __init__(self, docs):
        self._docs = docs


    def uniqueAttribs(self, xpath):
        """Return a list of attributes that uniquely distinguish the element at each segment"""
        acceptedAttribs = []
        # select examples which contain the relevant xpath
        docs = [doc for doc in self._docs if doc.tree().xpath(xpath.get())]
        for i, section in enumerate(xpath.walk()):
            sectionElements = flatten([doc.tree().xpath(section) for doc in docs])
            siblingElements = flatten([[s for s in e.itersiblings() if s.tag == e.tag] for e in sectionElements])
            siblingAttribs = flatten([self.extractAttribs(e) for e in siblingElements])
            proposedAttribs = self.commonAttribs(sectionElements)
            acceptedAttribs.append([a for a in proposedAttribs if a not in siblingAttribs])
        return acceptedAttribs


    def extractAttribs(self, element):
        """Return a list of attributes for the element"""
        attribs = []
        #print element.attrib.items()
        for attrName, attrValue in element.attrib.items():
            # punctuation such as '/' and ':' can confuse xpath, so ignore attributes with these characters
            if not self.anyIn('/:', attrValue+attrName):# and attrName in ('id', 'lass'):
                attribs.append((attrName, attrValue))
        return attribs


    def commonAttribs(self, elements):
        """Return a list of common attributes among a group of elements"""
        common = defaultdict(int)
        for e in elements:
            for attrib in self.extractAttribs(e):
                common[attrib] += 1
        return [attrib for (attrib, count) in common.items() if count == len(elements)]

    def addAttribs(self, xpath, allAttribs):
        """Add attributes to xpath"""
        sections = []
        for i, (section, attribs) in enumerate(zip(xpath, allAttribs)):
            if attribs:
                section = re.sub('\[\d+\]', '', section)
            for attrib in attribs:
                if type(attrib) == int:
                    section += '[%d]' % attrib
                else:
                    section += "[@%s='%s']" % attrib
            xpath[i] = section
        return xpath

    def removeAttribs(self, xpath):
        """
        >>> HtmlAttributes([]).removeAttribs(htmlXpath("/a[1]/b[@class='abc']/c")).get()
        '/a[1]/b/c'
        """
        attribRE = re.compile('\[@.*?\]')
        for i, section in enumerate(xpath):
            xpath[i] = re.sub(attribRE, '', xpath[i])
        return xpath

    def anyIn(self, l1, l2):
        """Return values in l1 that exist in l2

        >>> anyIn([1,2], [2,3])
        2
        >>> anyIn([1,2], [3])
        
        """
        for v1 in l1:
            if v1 in l2:
                return v1
        return None

    def allIn(self, l1, l2):
        """Return true if all of first list is in second list

        >>> allIn([1,2], [2,3])
        False
        >>> allIn([1,2], [1,2])
        True
        """
        for v1 in l1:
            if v1 not in l2:
                return False
        return True

