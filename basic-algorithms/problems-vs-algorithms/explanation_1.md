<!--
Problem 1: Square Root of an Integer

Provide an explanation for your answer, clearly organizing your thoughts into 
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

There is a straight forward iterative solution for finding the floored root by adding up the odd numbers up to the number. However, that would have runtime of O(n^1/2) naturally. 

However, the problem requests a log(n) runtime which means that the problem space must be divided in a binary search fashion.

The condition to be a floored root, k, is such that k ** 2 <= number but (k+1) ** 2 > number.

So we start by dividing the target number by 2 and then continue to adjust it up or down by the estimate divided by two, but since integer division can go to 0 we do a check and set the adjust to 1 if that case happens.

Space is O(1), runtime is O(log(n))