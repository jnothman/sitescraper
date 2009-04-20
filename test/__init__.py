__all__ = [
    #'ASX', 
    #'ninemsn_weather',
    #'theage',
    #'amazon',

    'yahoo_search',
    #'linuxquestions',
    #'imdb',
]


for module in __all__:
    exec 'import ' + module
