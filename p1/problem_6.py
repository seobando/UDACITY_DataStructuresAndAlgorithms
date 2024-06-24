class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string.strip(" -> ")

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    union_set = set()

    current = llist_1.head
    while current:
        union_set.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        union_set.add(current.value)
        current = current.next

    union_list = LinkedList()
    for value in union_set:
        union_list.append(value)

    return union_list

def intersection(llist_1, llist_2):
    set1 = set()
    intersection_set = set()

    current = llist_1.head
    while current:
        set1.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        if current.value in set1:
            intersection_set.add(current.value)
        current = current.next

    intersection_list = LinkedList()
    for value in intersection_set:
        intersection_list.append(value)

    return intersection_list


# Test Case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Union Test Case 1:", union(linked_list_1, linked_list_2))
print("Intersection Test Case 1:", intersection(linked_list_1, linked_list_2))

# Test Case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Union Test Case 2:", union(linked_list_3, linked_list_4))
print("Intersection Test Case 2:", intersection(linked_list_3, linked_list_4))

# Test Case 3: Edge case with empty linked lists
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print("Union Test Case 3:", union(linked_list_5, linked_list_6))
print("Intersection Test Case 3:", intersection(linked_list_5, linked_list_6))

# Test Case 4: One empty linked list
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_4 = [1, 2, 3, 4, 5]
for i in element_4:
    linked_list_8.append(i)

print("Union Test Case 4:", union(linked_list_7, linked_list_8))
print("Intersection Test Case 4:", intersection(linked_list_7, linked_list_8))

# Test Case 5: Large linked lists
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_5 = list(range(1000))
element_6 = list(range(500, 1500))

for i in element_5:
    linked_list_9.append(i)

for i in element_6:
    linked_list_10.append(i)

print("Union Test Case 5:", union(linked_list_9, linked_list_10))
print("Intersection Test Case 5:", intersection(linked_list_9, linked_list_10))

