class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAng=defaultdict(list)

        for word in strs:
            key=''.join(sorted(word))
            groupAng[key].append(word)
        
        return list(groupAng.values())
