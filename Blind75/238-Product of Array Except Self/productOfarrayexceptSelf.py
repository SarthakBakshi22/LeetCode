class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productList=[]
        mul=1
        for i in nums:
            productList.append(mul)
            mul*=i
        mulP=1
        for i in range(len(nums)-1,-1,-1):
            productList[i]=productList[i]*mulP
            mulP*=nums[i]
        return productList
