#!/usr/bin/python3
"""MRU Caching Module"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.usage_order = []  # istifadə sırasını izləmək üçün

    def put(self, key, item):
        """Add an item to the cache (MRU logic)"""
        if key is None or item is None:
            return

        # Əgər açar artıq mövcuddursa, onun yeri yenilənir
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            # Əgər limit keçilirsə
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Ən son istifadə olunan (MRU) elementin açarı
                discard_key = self.usage_order[-1]
                print("DISCARD:", discard_key)
                del self.cache_data[discard_key]
                self.usage_order.pop()

            # Yeni elementi əlavə edirik
            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """Get an item by key (and update usage order)"""
        if key is None or key not in self.cache_data:
            return None

        # Ən son istifadə olunan kimi işarələyirik
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
