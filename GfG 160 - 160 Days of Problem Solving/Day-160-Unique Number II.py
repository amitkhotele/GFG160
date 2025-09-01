class Solution:
    def singleNum(self, arr):
        x = 0
        for n in arr: x ^= n
        a = b = 0
        for n in arr:
            (a, b) = (a ^ n, b) if n & (x & -x) else (a, b ^ n)
        return [a, b] if a < b else [b, a]
