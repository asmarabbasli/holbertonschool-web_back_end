#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching:
    """ BaseCaching defines:
      - cache_data dictionary
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize the cache """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))
