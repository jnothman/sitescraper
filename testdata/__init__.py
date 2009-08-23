# the available test cases
__all__ = [
    #'amazon',
    #'asx', 
    #'bom',
    #'checkdns',
    #'cnet',
    #'google_finance',
    #'google_search',
    #'imdb',
    #'msn_search',
    #'msn_weather',
    #'rottentomatoes',
    #'slashdot',
    #'stackoverflow',
    #'techsupportforums',
    #'theage',
    #'theonion',
    #'theaustralian',
    #'yahoo_weather',
    #'yahoo_finance',
    'ebay', # scrape works, but not when try..?
]
[
    'bbc_news',
    'linuxquestions',
    'ubuntuforums',
    'yahoo_search', # extra div in scraped
]


for module in __all__:
    exec 'import ' + module
