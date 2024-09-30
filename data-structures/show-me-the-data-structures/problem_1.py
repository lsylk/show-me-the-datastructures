from problem_6 import LinkedList, Node
from typing import Any, Optional

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
            The value to be associated with the key.
        """
        if self.get(key) == -1:
            if len(self.cache) >= self.capacity:
                tail = self.data.tail()
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
            assert self.data.head
            self.data.remove(self.data.head)
            self.cache[key] = self.data.prepend(value)
            self.revcache[self.cache[key]] = key


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


