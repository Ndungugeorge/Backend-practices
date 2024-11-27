##!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
    
class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = {}
    
    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item
        return self.cache_data
    
    def get(self, key):
        if key:
            return self.cache_data.get(key)
        else:
            return None
        
class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.key_idx= []

    def put(self, key, item):
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return key
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = self.key_idx.pop(0)
            del self.cache_data[discarded]
            print("DISCARD:{}".format(discarded))
        
        self.cache_data[key] = item
        self.key_idx.append(key)
    
    def get(self, key):
        
        return self.cache_data.get[key]
    
class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.key_idx = []
    
    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item
            self.key_idx.append(key)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = self.key_idx.pop(-1)
            del self.cache_data[discarded]
            print("DISCARD",discarded)
    def get(self, key):
        self.cache_data.get(key, None)

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()