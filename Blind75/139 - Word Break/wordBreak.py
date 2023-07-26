class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordBreak=[]
        # makeWord=''
        # for ch in s:
        #     makeWord=makeWord+ch
        #     if makeWord in wordDict:
        #         wordBreak.append(makeWord)
        #         s=s[len(makeWord):]
        #         if s in wordDict:
        #             makeWord=''
        #             break
        #         makeWord=''
        #     else:
        #         continue

        # if makeWord!='':
        #     return False
        # else:
        #     return True
        wBreak = [False]*len(s)
        for i in range(len(s)):
            for word in wordDict:
                if i < len(word)-1:
                    continue
                if i==len(word)-1 or wBreak[i-len(word)]:
                    if s[i-len(word)+1:i+1]==word:
                        wBreak[i]= True
                        break
        return wBreak[-1]
