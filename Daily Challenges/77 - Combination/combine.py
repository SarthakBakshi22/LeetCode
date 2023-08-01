class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # result=[]
        # combination=[]
        # pair=0
        # if n==k==1:
        #     return [[1]]
        # for num in range(1,n+1):
        #     combination.append(num)
        #     pair=num
        #     if k>1:
        #         while(pair+1<=n):
        #             combination.append(pair+1)
        #             if len(combination)==k:
        #                 if sorted(combination) not in result:
        #                     result.append(combination)
        #                 combination=[]
        #                 combination.append(num)
        #             pair+=1
        #     else:
        #         result.append(combination)
        #     combination=[]
        # return result
        result=[]
        combination=[]
        def backtrack(start):
            if len(combination) == k:
                result.append(combination[:])
                return
            for num in range(start, n + 1):
                combination.append(num)
                backtrack(num + 1)
                combination.pop()
        backtrack(1)
        return result
