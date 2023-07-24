class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        longAS = 2
        longSeq = [{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                ap = nums[i] - nums[j]
                longSeq[i][ap] = longSeq[j].get(ap, 1) + 1
                longAS = max(longAS, longSeq[i][ap])

        return longAS
