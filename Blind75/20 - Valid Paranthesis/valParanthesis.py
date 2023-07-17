class Solution:
    def isValid(self, s: str) -> bool:
        openingBrackets=['(','{','[']
        closingBrackets=[')','}',']']
        stack=[]
        for ch in s:
            if ch in openingBrackets:
                stack.append(openingBrackets.index(ch))
            elif ch in closingBrackets:
                if len(stack)!=0 and stack[-1] == closingBrackets.index(ch):
                    stack.pop(-1)
                else:
                    return False
        return len(stack)==0
