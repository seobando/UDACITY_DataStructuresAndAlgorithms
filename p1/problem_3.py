import heapq
import sys
from collections import Counter, namedtuple

# A class representing a Huffman Tree Node
class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data):
    if not data:
        return "", None

    # Calculate frequency of each character
    frequency = Counter(data)

    # Create a priority queue (min-heap) with initial nodes
    heap = [Node(char, freq, None, None) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq, node1, node2)
        heapq.heappush(heap, merged)

    tree = heap[0]

    # Generate Huffman codes
    codes = {}
    def generate_codes(node, code=""):
        if node:
            if node.char is not None:
                codes[node.char] = code
            generate_codes(node.left, code + "0")
            generate_codes(node.right, code + "1")
    
    generate_codes(tree)

    # Encode the data
    encoded_data = ''.join(codes[char] for char in data)

    return encoded_data, tree

def huffman_decoding(data, tree):
    if not data or not tree:
        return ""

    decoded_data = []
    node = tree

    for bit in data:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            decoded_data.append(node.char)
            node = tree

    return ''.join(decoded_data)

# Test cases
if __name__ == "__main__":
    # Test Case 1: General case
    a_great_sentence = "The bird is the word"
    print("Test Case 1")
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))
    print()

    # Test Case 2: Edge case with empty string
    print("Test Case 2")
    empty_string = ""
    encoded_data, tree = huffman_encoding(empty_string)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Encoded data:", encoded_data)
    print("Decoded data:", decoded_data)
    print()

    # Test Case 3: Edge case with a single character repeated
    print("Test Case 3")
    single_char_string = "aaaaaaa"
    encoded_data, tree = huffman_encoding(single_char_string)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Encoded data:", encoded_data)
    print("Decoded data:", decoded_data)
    print()

    # Test Case 4: Very large string
    print("Test Case 4")
    large_string = "a" * 10000 + "b" * 5000 + "c" * 2000
    encoded_data, tree = huffman_encoding(large_string)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the original data is: {}\n".format(sys.getsizeof(large_string)))
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The encoded data matches the original data:", large_string == decoded_data)

