Explanation of the implementation:

- The Node class represents a node in the Huffman tree, and it includes a comparison method to prioritize nodes with lower frequencies.
- The huffman_encoding function builds the Huffman tree, generates the Huffman codes, and encodes the input data using these codes.
- The huffman_decoding function decodes the encoded data using the Huffman tree.
- The test cases cover a general case, an edge case with an empty string, an edge case with a single repeated character, and a very large string to test the efficiency and correctness of the implementation.