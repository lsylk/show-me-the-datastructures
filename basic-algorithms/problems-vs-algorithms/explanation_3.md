<!--
Problem 3: Rearrange Array Digits

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

This problem description is confusing. Assuming it wants alternating digits summed together in descending order, then it makes sense to use merge sort to get O(nlog(n)) running time. It seems like they wanted the merge sort to sort the digits by magnitude rather than a natural integer sort. 

I made the mergeSort a bottom up iterative solution rather than recursive function which breaks down and builds the list back up. 

Merge sort is O(nlog(n)) and iterating over the sorted list takes (n).