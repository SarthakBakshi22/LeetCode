class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        longAlt=[]
        longAlt.insert(0,0)
        for ind,alt in enumerate(gain):
            longAlt.append(longAlt[ind]+alt)
        return max(longAlt)
