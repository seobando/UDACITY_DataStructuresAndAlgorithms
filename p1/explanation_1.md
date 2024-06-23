Explanation of the implementation:

- The LRU_Cache class uses an OrderedDict to store cache items. The OrderedDict maintains the order of insertion and allows us to quickly move keys to the end to mark them as recently used.
- The get method retrieves the value associated with the key if it exists in the cache, and moves the key to the end of the OrderedDict to mark it as recently used.
- The set method inserts a new key-value pair, and if the key already exists, it removes the old entry before reinserting it to mark it as recently used. If the cache is full, it removes the least recently used item (the first item in the OrderedDict).

This approach is efficient and leverages the built-in features of OrderedDict to manage the LRU order. The provided test cases ensure that the cache behaves correctly, including handling edge cases with small and empty caches and managing large values.