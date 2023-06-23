class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numPairs=[]

        for num1,num2 in enumerate(nums):
            differ = target - num2
            if differ in numPairs:
                return [numPairs.index(differ),num1]
            numPairs.append(num2)
        return
