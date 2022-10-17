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
