#!/usr/bin/env python3
"""LRUCache module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - Inherits from BaseCaching
      - Caching system
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache using LRU
        """
        if key is None or item is None:
            return

        # Check if the cache is full
        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = next(iter(self.cache_data))
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the new item to the cache_data
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data.pop(key)
        self.cache_data[key] = item

        return item
