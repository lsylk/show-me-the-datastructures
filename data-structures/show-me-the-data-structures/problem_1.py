from typing import Any, Optional

class Node:
    """
    A class to represent a node in a linked list.

    Attributes:
    -----------
    value : int
        The value stored in the node.
    next : Optional[Node]
        The reference to the next node in the linked list.
    """

    def __init__(self, value: int) -> None:
        """
        Constructs all the necessary attributes for the Node object.

        Parameters:
        -----------
        value : int
            The value to be stored in the node.
        """
        self.value: int = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
        --------
        str
            A string representation of the node's value.
        """
        return str(self.value)


class LinkedList:
    """
    A class to represent a singly linked list.

    Attributes:
    -----------
    head : Optional[Node]
        The head node of the linked list.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the LinkedList object.
        """
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.curr: Optional[Node] = None

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
        --------
        str
            A string representation of the linked list, with nodes separated by " -> ".
        """
        cur_head: Optional[Node] = self.head
        out_string: str = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string
    
    def __repr__(self) -> str:
        return str(self)

    def append(self, value: int) -> None:
        """
        Append a new node with the given value to the end of the linked list.

        Parameters:
        -----------
        value : int
            The value to be stored in the new node.

        >>> example = LinkedList()
        >>> for x in range(1,4):
        ...     example.append(x)
        >>> example
        1 -> 2 -> 3 -> 
        """
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        node: Node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        node.next.prev = node
        self.tail = node.next

    def prepend(self, value: int) -> Node:
        """
        Prepend a new node with a given value to the begining of the list.

        Parameters:
        -----------
        value : int
            The value to be stored in the new node.

        >>> test = LinkedList()
        >>> test.prepend(1)
        1
        >>> test
        1 -> 
        >>> test.prepend(2)
        2
        >>> test
        2 -> 1 -> 
        """
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return self.head
        
        newHead = Node(value)
        newHead.next = self.head
        self.head.prev = newHead
        self.head = newHead
        return self.head

    def remove(self, node: Node) -> Optional[Node]:
        """
        Remove a given node from a linked list or return nothing

        >>> example = LinkedList()
        >>> example.remove(None) is None
        True
        >>> for x in range(1,4):
        ...     example.append(x)
        >>> next = example.head.next
        >>> example.remove(next)
        2
        >>> example
        1 -> 3 -> 
        >>> example.remove(example.head)
        1
        >>> example
        3 -> 
        """
        if node is None:
            return

        if self.head == node:
            if node.next is not None:
                self.head = node.next
            else:
                self.head = None
                self.tail = None
        else:
            if node.next is None:
                assert node.prev
                node.prev.next = None
                self.tail = node.prev
            else:
                assert node.prev
                node.prev.next = node.next
                node.next.prev = node.prev
        return node

    # def tail(self) -> Optional[Node]:
    #     """
    #     Return the final item in the linked list
    #     >>> example = LinkedList()
    #     >>> example.tail() is None
    #     True
    #     >>> for x in range(1,4):
    #     ...     example.append(x)
    #     >>> example.tail()
    #     3
    #     """
    #     curr = self.head
    #     while curr is not None and curr.next is not None:
    #         curr = curr.next
    #     return curr

    def __iter__(self):
        self.curr = self.head
        return self

    def __next__(self):
        if self.curr is None:
            raise StopIteration
        result = self.curr.value 
        self.curr = self.curr.next
        return result

class LRU_Cache:
    """
    A class to represent a Least Recently Used (LRU) cache.

    Attributes:
    -----------
    capacity : int
        The maximum number of items the cache can hold.
    cache : dict[int, int]
        The dictionary to point to index
    data: LinkedList
    
    
    """

    def __init__(self, capacity: int) -> None:
        """
        Constructs all the necessary attributes for the LRU_Cache object.

        Parameters:
        -----------
        capacity : int
            The maximum number of items the cache can hold.
        """
        assert capacity > 0, "Capacity must be positive"
        self.capacity: int = capacity
        self.cache: dict[int, Node] = {}
        self.revcache: dict[Node, int] = {}
        self.data: LinkedList = LinkedList()


    def get(self, key: int) -> int:
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.

        Parameters:
        -----------
        key : int
            The key to be accessed in the cache.

        Returns:
        --------
        Optional[Any]
            The value associated with the key if it exists, otherwise -1.
        """
        node = self.cache.get(key)
        if node is not None:
                self.data.remove(node)
                self.cache[key] = self.data.prepend(node.value)
                return node.value
        else:
            return -1

    def set(self, key: int, value: int) -> None:
        """
        Set or insert the value if the key is not already present. When the cache reaches 
        its capacity, it should invalidate the least recently used item before inserting 
        a new item.

        Parameters:
        -----------
        key : int
            The key to be inserted or updated in the cache.
        value : int
            The value to be associated with the key, must be positive.
        """
        assert isinstance(key, int), "Invalid key input type"
        assert isinstance(value, int), "Invalid value input type"
        assert value >= 0, "Negative values reserved for missing keys"
        if self.get(key) == -1:
            if len(self.cache) >= self.capacity:
                tail = self.data.tail
                if tail is not None:
                    self.data.remove(tail)
                    kkey = self.revcache.get(tail)
                    assert kkey
                    del self.cache[kkey]
                    self.cache[key] = self.data.prepend(value)
                    self.revcache[self.cache[key]] = key
            else:
                self.cache[key] = self.data.prepend(value)
                self.revcache[self.cache[key]] = key
            
            return
        elif self.get(key) != value:
            # The key was found in the cache using get, but does not match the value we are setting it to
            #Therefore `get`` has moved the key/value to the head of the list
            assert self.data.head
            #the head should exist or else it is contradictory that we found a value 
            #However, the value does not match the new value being set, so we remove the node
            self.data.remove(self.data.head)
            #we now add the new value back as a new node
            # and update the cache which points from the key to the value node for the key
            self.cache[key] = self.data.prepend(value)
            # We update the reverse cache which points from a node to a key
            self.revcache[self.cache[key]] = key
            # neither the cache or the reverse cache should ever have problems with duplicates
            # the key should be unique and there should only be one node holding a value for a key


if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    assert our_cache.get(1) == 1   # Returns 1
    assert our_cache.get(2) == 2   # Returns 2
    assert our_cache.get(9) == -1  # Returns -1 because 9 is not in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)  # This should evict key 3
    assert our_cache.get(3) == -1  # Returns -1, 3 was evicted

    # Test Case 2
    test_cache = LRU_Cache(3)
    test_cache.set(2,3)
    test_cache.set(2,4)
    assert len(test_cache.cache) == 1
    assert test_cache.get(2) == 4

    # Test Case 3
    # Eviction extreme case
    test_cache2 = LRU_Cache(1)
    test_cache2.set(1,1)
    test_cache2.set(2,2)
    test_cache2.set(3,3)
    assert test_cache2.get(1) == -1
    assert test_cache2.get(2) == -1
    assert test_cache2.get(3) == 3

    # test Case 4
    # updated key is evicted
    test_cache3=LRU_Cache(2)
    test_cache3.set(1,1)
    assert len(test_cache3.cache) == 1
    test_cache3.set(1,2)
    assert len(test_cache3.cache) == 1
    test_cache3.set(2,2)
    assert len(test_cache3.cache) == 2
    test_cache3.set(3,3)
    assert len(test_cache3.cache) == 2
    assert test_cache3.get(1) == -1
    assert test_cache3.get(3) == 3
    assert test_cache3.get(2) == 2

    #test cases for invalid values
    test_bad = LRU_Cache(5)
    try:
        test_bad.set(None, 1)
    except AssertionError as err:
        assert repr(err) == "AssertionError('Invalid key input type')"

    try:
        test_bad.set(1, None)
    except AssertionError as err:
        assert repr(err) ==  "AssertionError('Invalid value input type')"

    try:
        test_bad.set(1, -2)
    except AssertionError as err:
        assert repr(err) == "AssertionError('Negative values reserved for missing keys')"

    test_bad.set(1,1)
    for i in range(0, 1_000_000):
        test_bad.get(1)
    assert len(test_bad.cache) == 1
    assert test_bad.get(1) == 1
    
    for i in range(0, 1_000_000):
        test_bad.set(1, i)
    assert len(test_bad.cache) == 1
    assert test_bad.get(1) == 999_999

    try:
        bad_cap = LRU_Cache(-10)
    except AssertionError as err:
        assert repr(err) == "AssertionError('Capacity must be positive')"

    test_duplicates = LRU_Cache(5)
    test_duplicates.set(999_999_999, 1)
    test_duplicates.set(1_000_000_000, 1)
    test_duplicates.set(2**32, 1)
    assert test_duplicates.get(999_999_999) == 1
    assert test_duplicates.get(1_000_000_000) == 1
    assert test_duplicates.get(2**32) == 1

    test_big = LRU_Cache(1_000_000)
    for i in range(0, 1_000_000):
        test_big.set(i, i)
    
    for i in range(0, 1_000_000):
        assert test_big.get(i) == i
