class Solution:
    def countBits(self, n: int) -> List[int]:
        bits=[]
        for num in range(0,n+1):
            binNum = bin(num)
            bits.append(binNum.count('1'))
        return bits
