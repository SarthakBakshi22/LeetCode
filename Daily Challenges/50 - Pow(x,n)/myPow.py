class Solution:
    def myPow(self, x: float, n: int) -> float:
        #Linear Approach - TLE 291/306
        # powX=x
        # signN=1
        # if n < 0:
        #     signN = -1
        #     n = abs(n)
        
        # if n==0:
        #     return 1
        # else:
        #     while(n-1>0):
        #         powX=powX*x
        #         n-=1

        # if signN == -1:
        #     return 1/powX
        # else:
        #     return powX 

    #-------------------------Binary Exponentation---------------------------
        if n==0:
            return 1
        
        if n < 0:
            n=-1*n
            x=1.0/x
        
        povX = 1
        while n!=0:
            if n%2==1:
                povX *=x
                n-=1
            x*=x
            n//=2
        return povX
