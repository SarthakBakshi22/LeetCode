class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneNum={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        letters=[""]
        result=[]
        if digits=="":
           return []
        for digit in digits:
            result=[]
            for letter in letters:
                for ch in phoneNum[digit]:
                    result.append(letter+ch)
            letters=result
        return letters
