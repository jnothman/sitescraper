__all__ = [
    #'amazon',
    'asx', 
    #'bbc_news',
    #'bom',
    #'checkdns',
    #'cnet',
    #'google_finance',
    #'google_search',
    #'imdb',
    #'linuxquestions',
    #'msn_search',
    #'msn_weather',
    #'rottentomatoes',
    #'slashdot',
    #'stackoverflow',
    #'techsupportforums',
    #'theage',
    #'theaustralian',
    #'theonion',
    #'ubuntuforums',
    #'yahoo_finance',
    #'yahoo_weather',

    #'ebay',
    #'yahoo_search',
]


for module in __all__:
    exec 'import ' + module
