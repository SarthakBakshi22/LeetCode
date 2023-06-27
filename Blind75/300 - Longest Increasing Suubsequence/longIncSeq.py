class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longLis=[0]*(len(nums))
        longLis[0]=1
        for ind in range(1,len(nums)):
            maxInd=0
            for newInd in range(0,ind):
                if(nums[ind]>nums[newInd]):
                    maxInd=max(maxInd,longLis[newInd])
            longLis[ind]=1+maxInd
        return max(longLis)
