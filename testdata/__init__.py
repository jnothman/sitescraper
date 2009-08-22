# the available test cases
__all__ = [
    #'amazon',
    #'asx', 
    #'bom',
    #'checkdns',
    #'cnet',
    #'google_finance',
    #'google_search',
    #'rottentomatoes',
    #'slashdot',
    #'techsupportforums',
    #'theaustralian',
    #'yahoo_weather',
    #'yahoo_finance',
    'theonion',
]
[
    'bbc_news',
    'ebay',
    'imdb',
    'linuxquestions',
    'msn_weather',
    'stackoverflow',
    'theage',
    'ubuntuforums',
    'yahoo_search',

    'msn_search',
]


for module in __all__:
    exec 'import ' + module
