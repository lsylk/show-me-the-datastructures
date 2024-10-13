<!--
Problem 2: Search in a Rotated Sorted Array

Provide an explanation for your answer, clearly organizing your thoughts into 
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

Basically after the array has been rotated the minimum element is no longer at 0 but is  instead somewhere towards the end of the array. Then from that element to the end is a sorted array, and from the beginning up to that element is another sorted array. 

We can find the minimum index in log(n) by doing a variation of binary search, where we look for the low element by checking if the half we are looking at is in order. If not then we look at the other half, and we repeat until found. 
It is also important that the problem specifies that no duplicates are allowed. If it is not true then, this algorithm might break on some lists.
As long as the the list is not empty then the minimum element exists, and it is the same as the pivot point for the rotated array. This means that all of the elements in the list that are to the right of and including the pivot point are less than or equal to the element to the left of pivot point. 
Essentially, the pivot point is the minimum element and it is always between the high and low, as they get closer together then they will converge to the pivot point.
If the low value is less than the high value, it means have found the pivot point. 


Once we have the minimum we can split the array into the begining of the original sorted array and the rest of the sorted array.

If the target is less than or equal to the final element of the beginning array then the target must be in that array, if it is in the original array. We then do binary search on that array, runtime is log(n). 

Likewise, if that is not the case we do binary search on the rest array. 

Run time is log(n)
Space is O(1)