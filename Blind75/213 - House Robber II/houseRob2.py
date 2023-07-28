class Solution:
    def rob(self, nums: List[int]) -> int:
        # maxRobE = maxAmtE = 0
        # maxRobO = maxAmtO = 0
        # for money in range(0,len(nums)-2):
        #     maxRobE, maxAmtE = maxAmtE, max(nums[money] + maxRobE, maxAmtE)

        # for money in range(1,len(nums)-1):
        #     maxRobO, maxAmtO = maxAmtO, max(nums[money] + maxRobO, maxAmtO)
        # return max(maxAmtE,maxAmtO)
        if len(nums)==1:
            return nums[0]
        houses1=nums[:-1]
        houses2=nums[1:]
        maxRob = maxAmt = 0
        maxRob2 = maxAmt2 = 0
        for money in houses1:
            maxRob, maxAmt = maxAmt, max(money + maxRob, maxAmt)
        for money in houses2:
            maxRob2, maxAmt2 = maxAmt2, max(money + maxRob2, maxAmt2)
        return max(maxAmt,maxAmt2)
