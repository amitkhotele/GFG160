class Solution:
    def findMin(self, arr):
        low, high = 0, len(arr)-1
        while low<high:
            if arr[low]<arr[high]:
                return arr[low]
            mid = low + ((high-low)//2)
            if arr[mid]>arr[high]:
                low=mid+1
            else:
                high=mid
        return arr[low]
