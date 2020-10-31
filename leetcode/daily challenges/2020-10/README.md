#  October 2020 LeetCoding Challenge
My submitted solutions, not the best, just the one I write when I solve the problem with no to few improvements (more or less like contests) to better see my improvements
> Any improvements will be done in the full problem set section

## Extra notes
|Number/Day|Complexity|Notes|
|-|-|-|
|1|log(N)|Done with binary search but expected deque + window|
|4|N^2|Have to better undersand others' solution|
|5|K|Instead of a moving bit mask, we can use directly xor property on next power of 2 minus 1 like this: <pre lang="python">((1 << N.bit_length()) - 1) ^ N</pre>|
|7|N|Saw an interesting solution based on deque|
|9|2^depth|Deserialize done iteratively and it is complexe for nearly no advantage|
|11||Unable to find a solution|
|13|N*log(N)|Merge sort is compatible with linked list and respect the follow up constraint|
|14|N|Follow the hint provided with the problem|
|15|N|Respect the follow up constraint and one pass, hard time to find the primary loop condition and it is not even usefull because we can just count the number of element we have already changed|
|16|log(N*M)|Given the conditions of the matrix, the search is the same as a flat array|
|18||Unable to find a solution|
|21||Not optimal, have to redo it with stack to avoid to iterate over zeros|
|22|N|traverse tree for each depth level until one node has no child|
|23||I don't know how to do it without TLE|
|25||Good intuition, wrong way to do it, I'm not worthy to put it here|
|26||It takes me some time to find this one but I like this solution, recursively check the overflow of the 2 cups above the one we want with memoization because some cups are checked more than one time|
|27|N|Respect the follow up constraint|
|29|N|can be simplified by grouping zeros|
|30||Unable to find a solution|
|31||Not really inspired for this one, code is not good but it complied with the follow up constraint by swapping 2 nodes in the tree until it is valid, probably less efficient than just compare the inorder list with its sorted version to find the 2 missplaced nodes. I have to read other's solutions|