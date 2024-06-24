# Efficiency

## Time Complexity

**LinkedList Operations:**

Append: The append method traverses the entire linked list to add a new element at the end. Thus, its time complexity is O(n), where 𝑛 is the number of nodes in the linked list.
Size: The size method also traverses the entire linked list to count the nodes, resulting in O(n) time complexity.

**Union Operation:**

First Traversal: It traverses the first linked list and adds each element to a set. This operation is O(n 1), where 𝑛1 is the number of nodes in the first linked list.
Second Traversal: It traverses the second linked list and adds each element to the same set. This operation is O(n2), where 𝑛2 is the number of nodes in the second linked list.
Creating the Resulting LinkedList: After creating the union set, it traverses the set to append each element to the resulting linked list. This operation is O(u), where 𝑢 is the size of the union set.

Total Time Complexity: Combining these, the overall time complexity of the union function is 𝑂(𝑛1 + 𝑛2 + 𝑢)

**Intersection Operation:**

First Traversal: It traverses the first linked list and adds each element to a set. This operation is 𝑂(𝑛1)
Second Traversal: It traverses the second linked list and checks each element against the first set. If the element exists in the set, it adds it to the intersection set. This operation is 𝑂(𝑛2).
Creating the Resulting LinkedList: After creating the intersection set, it traverses the set to append each element to the resulting linked list. This operation is  O(i), where 𝑖 is the size of the intersection set.

Total Time Complexity: Combining these, the overall time complexity of the intersection function is 𝑂(𝑛1 + 𝑛2 + 𝑖).

## Space Complexity

**LinkedList Operations:**

Append and Size methods use O(1) additional space since they only use a few pointers/variables.
Union Operation:

Set for Union: The union set can grow to the size of all unique elements from both linked lists, leading to 𝑂(𝑛1 + 𝑛2) space complexity.
Resulting LinkedList: The resulting linked list will also store 𝑢 unique elements, leading to 𝑂(𝑢) space complexity.
Total Space Complexity: Combining these, the overall space complexity of the union function is 𝑂(𝑛1 + 𝑛2 + 𝑢).

**Intersection Operation:**

Set for First LinkedList: The set for the first linked list elements will take 𝑂(𝑛1) space.
Set for Intersection: The intersection set will take O(i) space.
Resulting LinkedList: The resulting linked list will store 𝑖 unique elements, leading to 𝑂(𝑖) space complexity.
Total Space Complexity: Combining these, the overall space complexity of the intersection function is 𝑂(𝑛1 + 𝑖).

## Code Design

**LinkedList Design:**

The linked list implementation is straightforward, using a Node class to store values and pointers to the next node.
The design allows for easy addition of elements at the end but does not optimize for operations like search, delete, or random access.

**Union and Intersection Functions:**

Union: Uses a set to collect unique elements from both linked lists, ensuring no duplicates in the resulting linked list.
Intersection: Uses a set to store elements from the first linked list and then checks for common elements in the second linked list to form the intersection set.

Both functions use sets for efficient membership testing, making the operations more efficient than naive methods.

**Resulting Linked Lists:**

The functions return new linked lists representing the union and intersection, preserving the original linked lists. This is a good design choice for immutability and side-effect-free operations.
