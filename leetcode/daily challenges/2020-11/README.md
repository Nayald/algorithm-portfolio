#  November 2020 LeetCoding Challenge
My submitted solutions, not the best, just the one I write when I solve the problem with no to few improvements (more or less like contests) to better see my improvements
> Any improvements will be done in the full problem set section

## Extra notes
|Number/Day|Complexity|Notes|
|-|-|-|
|4||I don't know how to do it without TLE|
|6|N*log(N)|Init left boundary with ⌈sum(nums) / threshold⌉ since we can write sum(nums) / threshold <= d|
|7||Reverse the two lists then add then reverse the result|
|10||Can also be done in place|
|13||q contains a list of each level separated by a None|
|14||I think I can explain the logic behind the solution but I find it by looking some results outputed by the website notably when 2nd and 3rd parameters are equal it gives ⌈log2 of the 1st parameter⌉|
|17||I am sure we can do better with something like Thales's theorem where the lenght % 2 is the side and height % 2 the choice between 0 and 1 for the right side (all in "p" unit) but I miss something to do it|
|19||I missread a bit the problem yet it work fine|
|20||binary search but fail to find a solution|
|21||two steps: first, for any number with less digits it can be any possible combinations, then, we have to calculate possible cases where leftmost digit(s) are in the list|