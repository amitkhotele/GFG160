class Solution:
    def missingNum(self, a):
        x = 0
        for i, v in enumerate(a): x ^= v ^ (i + 1)
        return x ^ (len(a) + 1)
