class Solution:
    def numDecodings(self, s: str) -> int:
        strLen = len(s)
        if strLen == 0 or s[0] == '0':
            return 0
        numDecodes = [1, 1]
        for i in range(1, strLen):       
            curWays = 0
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                curWays += numDecodes[-2]
            if s[i] != '0':
                curWays += numDecodes[-1]                
            if curWays == 0:
                return 0
            numDecodes.append(curWays)
        return numDecodes[-1]
