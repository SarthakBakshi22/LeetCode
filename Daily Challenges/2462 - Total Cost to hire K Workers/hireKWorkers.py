class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        minCost = 0
        n = len(costs)
        firstHalf = []
        secondHalf = []
        left, right = 0, n - 1

        for _ in range(k):
            while len(firstHalf) < candidates and left <= right: heappush(firstHalf, costs[left]); left+=1
            while len(secondHalf) < candidates and left <= right: heappush(secondHalf, costs[right]); right-=1

            a = firstHalf[0] if firstHalf else maxsize
            b = secondHalf[0] if secondHalf else maxsize

            if a <= b: minCost += a; heappop(firstHalf)
            else: minCost += b; heappop(secondHalf)
        return minCost 
