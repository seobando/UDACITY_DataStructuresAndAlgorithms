from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value  # reinsert the key to mark it as recently used
            return value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # remove the first (least recently used) item
        self.cache[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)  # returns 1
our_cache.get(2)  # returns 2
our_cache.get(9)  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(
    3
)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
cache_single = LRU_Cache(1)
cache_single.set(1, 1)
assert cache_single.get(1) == 1  # returns 1
cache_single.set(2, 2)
assert cache_single.get(1) == -1  # returns -1 because 1 was evicted
assert cache_single.get(2) == 2  # returns 2
## Test Case 2
empty_cache = LRU_Cache(2)
assert empty_cache.get(1) == -1  # returns -1 because cache is empty
## Test Case 3
large_cache = LRU_Cache(3)
large_cache.set(1, "a" * 1000)  # very large string value
large_cache.set(2, "b" * 1000)
large_cache.set(3, "c" * 1000)
assert large_cache.get(1) == "a" * 1000  # returns the large string
large_cache.set(4, "d" * 1000)
assert large_cache.get(2) == -1  # returns -1 because 2 was evicted