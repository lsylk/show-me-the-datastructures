
## Reasoning Behind Decisions:
It's a direct recursive solution for navigating a file tree. It has to inspect all files and folders in the tree. 

## Time Efficiency:
O(n) - base strictly on the number of files/folders contained recursively in the given path

## Space Efficiency:
O(n) - If all files in the path contain the correct suffix then it would be O(n) upper bound.