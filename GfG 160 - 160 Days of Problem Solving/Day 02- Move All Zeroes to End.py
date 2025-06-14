class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        nonZeroIndex = 0

        for i in range(n):
            if arr[i] != 0:
                arr[nonZeroIndex], arr[i] = arr[i], arr[nonZeroIndex]
                nonZeroIndex += 1
