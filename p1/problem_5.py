import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{self.timestamp}{self.data}{self.previous_hash}".encode("utf-8")
        sha.update(hash_str)
        return sha.hexdigest()


# Test Case 1: General case
block1 = Block(datetime.now(), "First block", "0")
print(f"Block 1 hash: {block1.hash}")

# Test Case 2: Edge case with empty data
block2 = Block(datetime.now(), "", block1.hash)
print(f"Block 2 hash: {block2.hash}")

# Test Case 3: Edge case with null data and timestamp
block3 = Block(None, None, None)
print(f"Block 3 hash: {block3.hash}")

# Test Case 4: Edge case with very large data
large_data = "a" * 1000000  # 1 million characters
block4 = Block(datetime.now(), large_data, block2.hash)
print(f"Block 4 hash: {block4.hash}")

# Test Case 5: Different data and same previous hash
block5 = Block(datetime.now(), "Some other data", block2.hash)
print(f"Block 5 hash: {block5.hash}")

# Check if the hash is different for different data but same previous hash
assert block4.hash != block5.hash, "Hashes should be different for different data"
