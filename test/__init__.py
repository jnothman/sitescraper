__all__ = [
    #'amazon',
    #'ASX', 
    #'bbc_news',
    #'BOM',
    #'google_search',
    #'msn_weather',
    #'rottentomatoes',
    #'slashdot',
    #'theage',
    #'theaustralian',
    #'theonion',
    #'ubuntuforums',
    #'yahoo_finance',
    #'yahoo_weather',

    #'msn_search',
    #'ebay',
    'google_finance',
    #'imdb',
    #'linuxquestions',
    #'stackoverflow',
    #'yahoo_search',
]


for module in __all__:
    exec 'import ' + module
