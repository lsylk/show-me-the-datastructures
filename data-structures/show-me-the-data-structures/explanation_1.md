
## Reasoning Behind Decisions:
I decided to use linked list implementation and dictionary lookups as they will provide the needed time complexity and behavior.
Linked list remove and prepend operations take O(1) time.
The cache lookups and updates/inserts also take O(1) time so overall the time complexity for get and set is O(1). 

## Time Efficiency:
get() - O(1)
set() - O(1)
## Space Efficiency:
O(n) - The cache, reversecache, and data linked list all will take O(n) space so overall the space complexity is O(n)
