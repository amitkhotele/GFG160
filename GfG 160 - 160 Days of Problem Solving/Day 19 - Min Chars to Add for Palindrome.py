class Solution:
    def minChar(self, s):
        n = len(s)

        rev_str = s[::-1]

        combined = s + "$" + rev_str

        lps = [0] * len(combined)
        for i in range(1, len(combined)):
            j = lps[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j

        return n - lps[-1]
