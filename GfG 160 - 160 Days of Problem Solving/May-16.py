import heapq

class Solution:
    def findSmallestRange(self, arr):
        k = len(arr)
        n = len(arr[0])
        
        # Initialize heap and max_val
        heap = []
        max_val = float('-inf')
        
        # Push the first element of each list into the heap
        for i in range(k):
            val = arr[i][0]
            heapq.heappush(heap, (val, i, 0))
            max_val = max(max_val, val)
        
        # Initialize the result range
        min_range = float('inf')
        start, end = -1, -1
        
        while True:
            min_val, row, col = heapq.heappop(heap)
            
            # Update the best range
            if max_val - min_val < min_range:
                min_range = max_val - min_val
                start, end = min_val, max_val
            
            # If there is a next element in the same row, push it into the heap
            if col + 1 < n:
                next_val = arr[row][col + 1]
                heapq.heappush(heap, (next_val, row, col + 1))
                max_val = max(max_val, next_val)
            else:
                # We've reached the end of one list, cannot proceed
                break
        
        return [start, end]
