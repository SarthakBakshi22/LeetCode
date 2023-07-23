class Solution:
    def longestPalindrome(self, s: str) -> str:
        # palinSubString=[]
        # maxLen=1
        # resString = [s[i: j] for i in range(len(s))
        #                 for j in range(i+1,len(s)+1)]
        # print(resString)
        # for subs in resString:
        #     if subs == subs[::-1] and len(subs) > maxLen:
        #         palinSubString.append(subs)
        # if len(palinSubString)==0:
        #     return s[0]

        # return max(palinSubString)
        # subCount=[]
        # longPal = ''
        # while(len(s)>0):
        #     palStr=''
        #     for ch in s:
        #         palStr=palStr+ch
        #         if palStr==palStr[::-1]:
        #             subCount.append(palStr)
        #             # if len(palStr)>len(longPal):
        #             #     longPal=palStr
        #     s=s[1:]
        # subCount.sort(key=len)
        # return subCount[-1]
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]

        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1] 
        return longest_palindrom
