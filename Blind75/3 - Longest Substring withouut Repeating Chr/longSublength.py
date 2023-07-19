class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen=0
        comSub=[]
        for ch in s:
            if ch in comSub:
                if comSub.index(ch)==0:
                    del(comSub[0])
                else:
                    comSub=comSub[comSub.index(ch)+1:]
                comSub.append(ch)
            else:
                comSub.append(ch)
                maxLen=max(maxLen,len(comSub))
        return maxLen
