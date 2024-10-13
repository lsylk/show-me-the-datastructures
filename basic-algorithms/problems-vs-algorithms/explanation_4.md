<!--
Problem 4: Dutch National Flag Problem

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

The Dutch flag red, white, and blue which map to 0,1,2.
The Blue should be placed at the end of the list, after the red and white. Therefore the blue elements should occupy the last |blue| slots after the the sum of the |red|+|white| elements. 

We only need to iterate over the list once because as we iterate we place the blue elements at the end and the red elements at the begining. Then as we continue to do that the white elements get shifted to the middle.

Running time is O(n)