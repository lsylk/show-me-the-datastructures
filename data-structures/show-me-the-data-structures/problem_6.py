from typing import Optional

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
            return

        node: Node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

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
            return self.head
        
        newHead = Node(value)
        newHead.next = self.head
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
        curr = self.head
        if curr == node and self.head is not None:
            self.head = self.head.next
            return curr

        while curr is not None and curr.next != node:
            curr = curr.next

        if curr is None:
            return
        else:
            curr.next = node.next
            return node
        
    def index(self, n: int) -> Optional[Node]:
        """
        Returns a node equivalent to list index in LinkedList or None

        >>> example = LinkedList()
        >>> for x in range(1,4):
        ...     example.append(x)
        >>> example.index(0)
        1
        >>> example.index(2)
        3
        >>> example.index(10) is None
        True
        """
        i = 0
        curr = self.head
        while curr is not None and i != n:
            curr = curr.next
            i = i + 1
        return curr


    def size(self) -> int:
        """
        Calculate the size (number of nodes) of the linked list.

        Returns:
        --------
        int
            The number of nodes in the linked list.

        >>> example = LinkedList()
        >>> example.size()
        0
        >>> for x in range(1,4):
        ...     example.append(x)
        >>> example.size()
        3
        """
        size: int = 0
        node: Optional[Node] = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def tail(self) -> Optional[Node]:
        """
        Return the final item in the linked list
        >>> example = LinkedList()
        >>> example.tail() is None
        True
        >>> for x in range(1,4):
        ...     example.append(x)
        >>> example.tail()
        3
        """
        curr = self.head
        while curr is not None and curr.next is not None:
            curr = curr.next
        return curr

    def __iter__(self):
        self.curr = self.head
        return self

    def __next__(self):
        if self.curr is None:
            raise StopIteration
        result = self.curr.value 
        self.curr = self.curr.next
        return result


def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the union of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all unique elements from both input linked lists.
    """
    # Use a set to store all unique elements
    left = set(llist_1)
    right = set(llist_2)
    list_union = left.union(right)
    # Create a new linked list to store the union
    result = LinkedList()
    for elem in list_union:
        #it is more efficient to prepend but for the sake of preserving order, append
        result.append(elem)
    return result
    

def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the intersection of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all elements that are present in both input linked lists.
    """
    # Use sets to find the intersection
    # Find the intersection of both sets
    # Create a new linked list to store the intersection
    left = set(llist_1)
    right = set(llist_2)
    list_intersection = left.intersection(right)
    # Create a new linked list to store the union
    result = LinkedList()
    for elem in list_intersection:
        result.append(elem)
    return result

def tests():
    ## Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    
    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Test Case 1:")
    print("Union:", union(linked_list_1, linked_list_2)) # Expected: 1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65
    print("Intersection:", intersection(linked_list_1, linked_list_2)) # Expected: 4, 6, 21
    assert set(union(linked_list_1, linked_list_2)) == { 1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65 }
    assert set(intersection(linked_list_1, linked_list_2))  == { 4, 6, 21 }

    ## Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("\nTest Case 2:")
    print("Union:", union(linked_list_3, linked_list_4)) # Expected: 1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65
    print("Intersection:", intersection(linked_list_3, linked_list_4)) # Expected: empty
    assert set(union(linked_list_3, linked_list_4)) == { 1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65 }
    assert set(intersection(linked_list_3, linked_list_4)) == set([])

    ## Test case 3
    ll_5 = LinkedList()
    ll_6 = LinkedList()
    
    for i in element_1:
        ll_6.append(i)
    assert set(union(ll_5, ll_6)) == set(element_1)
    assert set(intersection(ll_5, ll_6)) == set([])

    ## Test case 4
    assert set(union(ll_6, ll_6)) == set(element_1)
    assert set(intersection(ll_6, ll_6)) == set(element_1)
    



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    tests()