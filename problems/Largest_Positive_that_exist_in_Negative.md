## Problem Statement:
You are given an array of integers (includes both positive and negative numbers). 
<br>You have to find largest positive and negative.


## Input : 

-3  -1  1  3

## Output : 

3

<br>Explanation: The largest positive is 3  and then it exist in  negative.

```
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        res=-1
        lo=len(nums)
        r=lo-1
        l=0
        while(l<r):
            tot=nums[r]+nums[l]
            if tot==0:
                res=nums[r]
                break
            elif tot>0:
                r-=1
            else:
                l+=1
        return res
```
