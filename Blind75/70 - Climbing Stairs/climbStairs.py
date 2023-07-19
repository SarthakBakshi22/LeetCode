class Solution:
    def climbStairs(self, n: int) -> int:
        step1=1
        step2=2
        if n <= 3:
            return n
        for _ in range(3, n + 1):
            step2, step1 = step2 + step1, step2
        
        return step2
