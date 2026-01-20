Approach

Brute force:
1. Nested for loop
2. For each value, check if added with all other values, when is it equal to target.
3. Iterate through every value until corresponding values found.

One pass hashmap:
1. Create an empty hashmap
2. Using a for loop, iterate through the given array
3. Calculate the difference between target and current item
4. Check if difference is found in hashmap
5. If it is, return the index of that item and the current index
6. Else, add that item to the hashmap with the current item as key and index as value. <item>:<index>
