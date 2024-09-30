
## Reasoning Behind Decisions:
The problem specified that a linked list was to be used. It might be nice to make the nodes immutable but I'm not sure how to do that. 

Overall, I tried to use the python interfaces which made it easy to convert between using a list() and a LinkedList.

## Time Efficiency:
O(n) - Iterating over the list will take linear time.
O(1) - Adding another item to the list will take constant time assuming sha256 is also constant time. Probably since data is a string which it must evaluate then it might take O(n)

## Space Efficiency:
O(n)