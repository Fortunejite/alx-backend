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
        self.least_recently_used = ''

    def get_least_recently_used(self):
        least = next(iter(self.cache_data))
        for key in self.cache_data:
            if self.cache_data[key][0] > self.cache_data[least][0]:
                least = key
        return least

    def put(self, key, item):
        """ Add an item in the cache using LRU
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    least = self.get_least_recently_used()
                    print("DISCARD: {}".format(least))
                    del self.cache_data[least]
            self.cache_data[key] = [1, item]

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data[key][0] += 1
            return self.cache_data[key][1]
        return None
    
    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)[1]))
