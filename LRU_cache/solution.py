"""
I need to implement a class that follows the constraints of an LRU (least recently used) cache. In an LRU cache, when I add a new key to
the cache, if the cache's size has been exceeded, I must evict the least recently used element from the cache.

I can use a map to store key-value pairs allowing get operations to happen in O(1) time. How can I track the least recently used element
in the data structure? The least recently used element will be the element that hasn't been used in the longest amount of time. It would
be great if there was a way to track which elements had been used, and trickle down the least used elements. The put operation needs to run
in O(1) time which means the evict operation also needs to be done in O(1) time.

I can use a doubly linked list to accomplish keeping track of the LRU element using a "trickle down" approach. Whenever I interact with
an element, either by adding or getting it, I move the element to the head of the list. Elements that are not used get moved towards the
back of the list as more frequently used elements keep getting pushed to the head. When I need to evict an element, I simply drop the tail.
To help with this, I keep track of both the head and the tail. This way, the structure uses O(n) memory, where n is the size of the cache,
but adding, putting and evicting elements is O(1) because adding or removining individual elements from a double linked list is O(1) as
is any operation on a hash map.
"""

class ListNode:
    def __init__(self, val, _next=None, prev=None):
        self.val = val
        self.next = _next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # Initialize the map and linked list
        # This map will point to a tuple of the value stored at the key, as well as its node representation
        self.map = {}
        self.head, self.tail = None, None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map.keys():
            return -1
        val, node = self.map[key]
        self._make_node_head(node)
        return val

    def put(self, key: int, value: int) -> None:
        # Update the key value in the list. I need to handle a few cases here. First, if the key exists in the map already, I need to
        # update the value in the map. Note that the list does not store values, it stores keys to the map which stores the values.
        # Therefore, on updates, I do not need to update the list. Additionally, if the key exists, I need to perform the same udpate as
        # in get to move this node to the head of the list.
        # 
        # If the key does not exist, I need to add it to the structure. If the structure is empty, I simply create a new node and set the
        # head and tail of the list to this new node. If the structure is not empty, I create a new node and set this node as the new head
        # of the list

        # Handle the case where the key does not exist in the structure first
        if key not in self.map.keys():
            node = ListNode(key)
            # Check to see if the map is empty
            if len(self.map.keys()) == 0:
                # Add the value to the list and create a node, setting the head and tail pointers to this node
                self.head = node
                self.tail = node
            else:
                # Simply set this new node to be the new head
                node.next = self.head
                self.head.prev = node
                self.head = node
            self.map[key] = (value, node)
            
            # I need to check if the capacity of the cache has been exceeded
            if len(self.map.keys()) > self.capacity:
                # I need to remove the key stored at tail
                drop_key = self.tail.val
                self.tail = self.tail.prev
                self.tail.next = None
                del self.map[drop_key]
        # Handle case where node exists in structure already
        else:
            _, node = self.map[key]
            self._make_node_head(node)
            self.map[key] = (value, node)
    
    def _make_node_head(self, node):
        """
        Update the head of the list to be this element. A few things have to happen here. First, I need to check if this node is the
        head of the list. If it is the current head of the list, I simply return the value. If it is not the head of the list, I need to
        make some checks. I check if this node is the tail of the list. If so, I update the tail of the list to point to this
        nodes previous node. I then set that nodes next pointer to be None. If the node is neither the head or the tail, I need to remove
        it such that the nodes preivous pointer points to its next pointer and the nodes next previous pointer points to this nodes
        previous pointer. I keep a copy of this node. Once this is done, I make this node the new head by pointing its previous pointer
        to None and its next pointer to the lists current head. I then move the head pointer to this node
        """
        # Check to see if this node is the head of the list. If so, do nothing
        if node != self.head:
            # Check to see if this node is the tail
            if node == self.tail:
                # Make the new tail this nodes previous pointer and change that nodes next pointer to null
                self.tail = node.prev
                node.prev.next = None
            else:
                # Update the nodes previous and next pointers. 
                node.prev.next = node.next
                node.next.prev = node.prev
            # Update the nodes pointer to be the current head, update the head pointer and set its previous pointer to null
            node.next = self.head
            self.head.prev = node
            self.head = node
            node.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
