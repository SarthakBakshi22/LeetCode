class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2*k + 1:
            return [-1] * len(nums)
        avgList = [-1] * k
        start = 0
        end = 2*k
        avg = sum(nums[0:2*k + 1])
        length = 2*k + 1
        while end < len(nums):
            avgList.append(avg//length)
            avg-=nums[start]
            start+=1
            end+=1
            if end < len(nums):
                avg+= nums[end]
        avgList +=  [-1] * k
        return avgList
