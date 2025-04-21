class Solution:
    def minRemoval(self, intervals):
        intervals.sort(key=lambda x: x[0])
        count, prevEnd = 0, intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                count += 1
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]

        return count
