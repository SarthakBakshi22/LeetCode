class Solution:
    def isPalindrome(self, s: str) -> bool:
        match = re.findall(r'[a-zA-Z0-9]*',s)
        s = "".join(match)
        s=s.lower()
        return s==s[::-1]
