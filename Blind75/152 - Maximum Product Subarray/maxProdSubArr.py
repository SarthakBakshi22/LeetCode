class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd=1
        minProd=1
        maxRes = nums[0]

        for num in nums:
            val=(num, num*maxProd, num*minProd)
            maxProd, minProd = max(val), min(val)
            maxRes = max(maxRes,maxProd)
        return maxRes
