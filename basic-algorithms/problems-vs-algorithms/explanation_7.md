<!--
Problem 7: Request Routing in a Web Server with a Trie

Provide an explanation for your answer, clearly organizing your thoughts into 
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

The Route Trie is very similar to the Trie in the examples and problem 5. However,
This time the dictionary keys are parts of paths rather than individual chars.

The runtime and space complexity is basically O(n) where n is number of parts in a path.

I added type assertions to the function in case someone ignores the mypy types, which should prevent nonsense situations. It is better to fail loudly and early rather than silently and late at runtime.

There wasn't a prewritten test for the root route. It made sense to add one and then to differentiate it from an empty string I added a check for the path to begin with '/' which also doubles as a check for a valid route anyway. 