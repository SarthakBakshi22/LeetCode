class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jmp=0
        for ind,jp in enumerate(nums):
            if jmp < ind:
                return False
            jmp=max(jmp,jp+ind)
        return True
