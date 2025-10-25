#!/usr/bin/python3
""" LIFO caching module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.last_key = None  # Ən son əlavə olunan açarı yadda saxlayırıq

    def put(self, key, item):
        """ Add an item to the cache (LIFO algorithm) """
        if key is None or item is None:
            return

        # Əgər artıq bu açar varsa, sadəcə yenilə və çıx
        if key in self.cache_data:
            self.cache_data[key] = item
            self.last_key = key
            return

        # Yeni element əlavə edirik
        self.cache_data[key] = item

        # Əgər limit keçilirsə
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Ən son əlavə olunan açarı sil
            del self.cache_data[self.last_key]
            print(f"DISCARD: {self.last_key}")

        # Ən son əlavə olunan açarı yadda saxla
        self.last_key = key

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
