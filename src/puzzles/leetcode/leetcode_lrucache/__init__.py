# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
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

# SOLVED
# dictonary plus linked list for constant time access and edits

class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.size = 0
        self.cap = capacity

        # sentinel nodes for doubly linked list
        self.back = Node(None, None)
        self.front = Node(None, None)

        self.back.next = self.front
        self.front.prev = self.back

        self.d = {}  # maps key to NODE, not value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            # move node to front
            node = self.d[key]

            self.unlink_node(node)
            self.add_front(node)

            return node.val
        else:
            return -1

    def unlink_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_front(self, node):
        node.next = self.front
        node.prev = self.front.prev

        node.prev.next = node
        node.next.prev = node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.unlink_node(node)
        else:
            if self.size == self.cap:
                # remove links to LRU
                node = self.back.next
                del self.d[node.key]
                self.unlink_node(node)
            else:
                self.size += 1

            # create new node
            node = Node(key, value)
            self.d[key] = node
        self.add_front(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)