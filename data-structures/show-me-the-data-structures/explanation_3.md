
## Reasoning Behind Decisions:
There really wasn't much to decide here. The types and function definitions provided the constrains of the implementation.

The only choice I made was for the build_huffman_tree for an empty str or a str with 1 character that a Huffman node should be returned. This allowed encoding those types of strings otherwise I got a runtime error.

## Time Efficiency:
calculate_frequencies - O(n)
The build_huffman_tree takes n*log(n) time because every heap pop and push takes log(n) time and we must iterate over every node generated from frequencies keys.
huffman_encoding takes n*log(n) because of the above
huffman_decoding - O(n * log(n)) because the height of the tree is log(n) and for every character will require traversing from the top of the tree to a root.

## Space Efficiency:
O(n) - Basically the whole list if each character was unique, but typically less