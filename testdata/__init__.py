# the available test cases
__all__ = [
    'amazon',
    'asx', 
    'bbc_news',
    'bom',
    'checkdns',
]
[
    'cnet',
    'ebay',
    'google_finance',
    'google_search',
    'imdb',
    'linuxquestions',
    'msn_search',
    'msn_weather',
    'rottentomatoes',
    'slashdot',
    'stackoverflow',
    'techsupportforums',
    'theage',
    'theaustralian',
    'theonion',
    'ubuntuforums',
    'yahoo_finance',
    'yahoo_search',
    'yahoo_weather',
]


for module in __all__:
    exec 'import ' + module
