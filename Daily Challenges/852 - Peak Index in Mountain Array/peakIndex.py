class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # mid = len(arr)//2
        # peak=0
        # if arr[mid] > arr[mid+1]:
        #     for ind,num in enumerate(arr[:mid+1]):
        #         peak = max(peak,num)
        #     return arr.index(peak)
        # else:
        #     for ind,num in enumerate(arr[mid+1:]):
        #         peak = max(peak,num)
        #     return arr.index(peak)
        start=0
        end=len(arr)-1
        while start < end:
            peak = (start+end)//2
            if arr[peak]>arr[peak+1]:
                end=peak
            else:
                start = peak+1
        return start
