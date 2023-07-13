class Solution:
    def reverseBits(self, n: int) -> int:
        newBit=''
        for bt in format(n,'032b'):
            newBit=newBit+str(bt)
        newBit = newBit[::-1]
        return int(newBit,2)
