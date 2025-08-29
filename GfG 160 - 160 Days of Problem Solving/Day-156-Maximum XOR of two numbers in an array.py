class Solution:
    def maxXor(self, arr):
        max_xor, mask = 0, 0
        for i in range(30, -1, -1):
            mask |= (1 << i)
            prefixes = set()
            temp = max_xor | (1 << i)
            found = False
            for num in arr:
                prefix = num & mask
                if (temp ^ prefix) in prefixes:
                    found = True
                    break
                prefixes.add(prefix)
            if found:
                max_xor = temp
        return max_xor
