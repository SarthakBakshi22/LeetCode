class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totSum = sum(nums)
        nsum = n*(n+1)/2
        return int(abs(nsum-totSum))
