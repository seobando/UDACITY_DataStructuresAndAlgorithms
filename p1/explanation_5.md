# Efficiency:

## Time Efficiency:

The code to create a hash for a block runs in constant time  O(1). This is because the operations performed (concatenating strings and hashing) do not depend on the size of the blockchain.
The time complexity for the calc_hash method, which is the most computationally intensive part, is O(1). The SHA-256 hashing algorithm used here runs in constant time relative to the size of the input, which is fixed.

## Space Efficiency:

The space complexity is also O(1) for each block. Each block stores a timestamp, data, previous hash, and its own hash. Assuming that the size of data is bounded or small, this results in constant space usage per block.
The total space complexity for the entire blockchain will be O(n) where n is the number of blocks in the chain because each block's space is constant.
Code Design:

# Choice of Algorithm:

The SHA-256 hashing algorithm is chosen for its cryptographic security properties, making it suitable for ensuring the integrity and uniqueness of each block's hash.
Choice of Data Structure:

A simple class structure (Block) is used to represent each block in the blockchain, which makes the code easy to understand and maintain.
The design implicitly suggests a singly linked list structure where each block points to the previous one via the previous_hash.
Design Considerations:

The constructor of the Block class immediately calculates the hash of the block upon instantiation, ensuring that each block is immutable once created.
There is no direct blockchain class, so linking blocks and managing the chain is assumed to be handled externally, which could be a limitation if block management logic is extensive.
