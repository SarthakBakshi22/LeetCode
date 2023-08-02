class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        if len(nums)==1:
            return [nums]
        else:
            result = list(itertools.permutations(nums))
        return [res for res in result]
