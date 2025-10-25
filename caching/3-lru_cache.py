#!/usr/bin/python3
""" LRU caching module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU (Least Recently Used) caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.usage_order = []  # istifadə sırasını saxlayırıq

    def put(self, key, item):
        """ Add an item to the cache (LRU algorithm) """
        if key is None or item is None:
            return

        # Əgər açar artıq mövcuddursa, sadəcə yeri yenilənir
        if key in self.cache_data:
            self.cache_data[key] = item
            # əvvəlki mövqedən sil, sona əlavə et
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return

        # Yeni açar əlavə edirik
        self.cache_data[key] = item
        self.usage_order.append(key)

        # Əgər limit keçilirsə (MAX_ITEMS = 4)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Ən az istifadə olunan (ən əvvəlki) açarı tapırıq
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Açar istifadə olundu, deməli ən son istifadə edilən olur
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
