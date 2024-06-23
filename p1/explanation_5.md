Explanation:

- calc_hash Method: This method constructs a string from the block's timestamp, data, and previous hash. It encodes this string to UTF-8 and generates a SHA-256 hash, which uniquely represents the block's contents.
- Block Class: The Block class initializes with a timestamp, data, and previous hash. It calculates its hash upon creation using the calc_hash method.