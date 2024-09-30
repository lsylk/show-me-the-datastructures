
## Reasoning Behind Decisions:
I decided to use linked list implementation and dictionary lookups as they will provide the needed time complexity and behavior.
Linked list remove and prepend operations take O(1) time.
The cache lookups and updates/inserts also take O(1) time so overall the time complexity for get and set is O(1). 

Edit: On reviewing I noticed that the current LinkedList operation is O(n) because I am iterating throught the list to find the previous node. However, if I change the linked list to a doubly linked list then the run time bounds would be correct, but it would complicated problem 6 so I did not change it. 
## Time Efficiency:
get() - O(1) //Actually O(n) with singly linked list, O(1) with doubly linked list
set() - O(1) //The same as above
## Space Efficiency:
O(n) - The cache, reversecache, and data linked list all will take O(n) space so overall the space complexity is O(n)
