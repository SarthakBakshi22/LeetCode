class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = []  
        priorityPair = []
        for num in nums1:
            heapq.heappush(priorityPair, [num + nums2[0], 0]) 
        while k > 0 and priorityPair:
            pair = heapq.heappop(priorityPair)
            s, pos = pair[0], pair[1] 
            pairs.append([s - nums2[pos], nums2[pos]])
            if pos + 1 < len(nums2):
                heapq.heappush(priorityPair, [s - nums2[pos] + nums2[pos + 1], pos + 1])

            k -= 1

        return pairs
