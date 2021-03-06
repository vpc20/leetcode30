# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following
# operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
#            otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
#                   When the cache reached its capacity, it should invalidate the least recently used item before
#                   inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# from collections import defaultdict
#
#
# class Node:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.next = None
#         self.prev = None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def prepend(self, key, val):
#         new_node = Node(key, val)
#         new_node.next = self.head  # old head
#         new_node.prev = None
#
#         if self.head is not None:  # old head
#             self.head.prev = new_node
#
#         self.head = new_node  # new node will always be the head
#         if self.tail is None:  # if doubly linked list is empty
#             self.tail = new_node  # new node will be both head and tail
#         return new_node
#
#     def append(self, key, val):
#         if self.head is None:  # empty list
#             return self.prepend(key, val)
#         else:
#             new_node = Node(key, val)
#             new_node.next = None
#             new_node.prev = self.tail  # old tail
#             self.tail.next = new_node  # old tail
#             self.tail = new_node  # new node will always be the tail
#             return new_node
#
#     def delete(self, node):
#         if self.head is None:  # empty list
#             return
#         key = node.key
#         if node == self.head:  # node.next will be the new head
#             self.head = node.next
#             # self.head.prev = None
#         elif node == self.tail:  # node.prev will be the new tail
#             self.tail = node.prev
#             self.tail.next = None
#         else:  # prev node and next node will be linked to each other
#             node.prev.next = node.next
#             node.next.prev = node.prev
#         del node
#         return key
#
#     def display_forward(self):
#         curr = self.head
#         while curr:
#             print(f'({curr.key}, {curr.val})', end=' ')
#             curr = curr.next
#         print('')
#
#
# class LRUCache:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.size = 0
#         self.dll = DoublyLinkedList()
#         self.key_nodes = defaultdict(Node)
#
#     def get(self, key):
#         if key not in self.key_nodes:
#             return -1
#         node = self.key_nodes[key]
#         key = node.key
#         val = node.val
#         if self.size == 1:
#             return val
#
#         delkey = self.dll.delete(node)
#         del self.key_nodes[key]
#
#         new_node = self.dll.append(key, val)
#         self.key_nodes[key] = new_node
#
#         return val
#
#     def put(self, key, value):
#         if key in self.key_nodes:
#             node = self.key_nodes[key]
#             node.val = value
#             self.get(key)
#             return
#
#         if self.size == self.capacity:
#             delkey = self.dll.delete(self.dll.head)  # head is least recently used
#             del self.key_nodes[delkey]
#         else:
#             self.size += 1
#         node = self.dll.append(key, value)  # tail is most recently used
#         self.key_nodes[key] = node
#
#     def display(self):
#         self.dll.display_forward()
from collections import OrderedDict


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class LRUCache(OrderedDict):

    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# lru_cache = LRUCache(2)
# lru_cache.put(1, 1)
# lru_cache.put(2, 2)
# print(lru_cache.get(1))
# lru_cache.put(3, 3)
# print(lru_cache.get(2))
# lru_cache.put(4, 4)
# print(lru_cache.get(1))
# print(lru_cache.get(3))
# print(lru_cache.get(4))

# lru_cache = LRUCache(1)
# lru_cache.put(2, 1)
# print(lru_cache.get(2))


lru_cache = LRUCache(2)
lru_cache.put(2, 1)
lru_cache.put(2, 2)
print(lru_cache.get(2))
lru_cache.put(1, 1)
lru_cache.put(4, 1)
print(lru_cache.get(2))
#
# lru_cache.display()
