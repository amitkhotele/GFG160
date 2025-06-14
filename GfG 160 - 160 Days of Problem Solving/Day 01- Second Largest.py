class Solution:
    def getSecondLargest(self, arr):
        first = float('-inf')
        second = float('-inf')

        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num < first:
                second = num

        return -1 if second == float('-inf') else second
