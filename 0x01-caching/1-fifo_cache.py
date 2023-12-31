#!/usr/bin/env python3
"""FIFOCache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - Inherits from BaseCaching
      - Caching system
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = next(iter(self.cache_data))
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
