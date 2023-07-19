class Solution:
    def countSubstrings(self, s: str) -> int:
        subCount=[]
        while(len(s)>0):
            palStr=''
            for ch in s:
                palStr=palStr+ch
                if palStr==palStr[::-1]:
                    subCount.append(palStr)
            s=s[1:]
        return len(subCount)
