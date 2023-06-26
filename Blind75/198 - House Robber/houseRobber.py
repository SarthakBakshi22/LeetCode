class Solution:
    def rob(self, nums: List[int]) -> int:
        maxRob = maxAmt = 0
        for money in nums:
            maxRob, maxAmt = maxAmt, max(money + maxRob, maxAmt)
        return maxAmt
