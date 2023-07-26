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
        self.last = ''

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    print("DISCARD: {}".format(self.last))
                    del self.cache_data[self.last]
            self.cache_data[key] = item
            self.last = key

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.last = key
            return self.cache_data[key]
        return None
