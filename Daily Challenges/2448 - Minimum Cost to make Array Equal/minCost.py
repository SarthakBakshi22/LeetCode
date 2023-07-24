class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        numcostPair = sorted(list(zip(nums,cost)))
        costMed = sum(cost)/2
        costT = 0
        for num,cst in numcostPair:
            costT +=cst
            if costT>=costMed:
                equalNum = num
                break
        costMin = 0
        for num,cst in numcostPair:
            costMin +=abs(num-equalNum)*cst
        return costMin
