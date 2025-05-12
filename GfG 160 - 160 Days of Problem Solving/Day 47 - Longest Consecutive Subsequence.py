class Solution:
    def longestConsecutive(self, arr):
        num_set = set(arr)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current, count = num, 1
                while current + 1 in num_set:
                    current += 1
                    count += 1
                longest = max(longest, count)

        return longest
