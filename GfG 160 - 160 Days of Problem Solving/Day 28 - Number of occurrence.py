class Solution:
    def countFreq(self, arr, target):
        import bisect
        low = bisect.bisect_left(arr, target)
        high = bisect.bisect_right(arr, target)
        return (high-low) if low<len(arr) and arr[low] == target else 0
