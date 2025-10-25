#!/usr/bin/python3
""" FIFO caching module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache (FIFO algorithm) """
        if key is None or item is None:
            return

        # Əgər artıq bu açar varsa, sadəcə yenilə
        self.cache_data[key] = item

        # Əgər limit keçilirsə (MAX_ITEMS = 4)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Ən birinci əlavə olunan açarı tap
            first_key = next(iter(self.cache_data))
            # Sil
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
