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