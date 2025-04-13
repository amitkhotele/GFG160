class Solution:
    def computeLPSArray(self, pat, m, lps):
        len = 0
        i = 1
        while i < m:
            if pat[i] == pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len != 0:
                    len = lps[len - 1]
                else:
                    lps[i] = 0
                    i += 1

    def search(self, pat, txt):
        result = []
        m = len(pat)
        n = len(txt)
        lps = [0] * m

        self.computeLPSArray(pat, m, lps)

        i = 0
        j = 0
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1

            if j == m:
                result.append(i - j)
                j = lps[j - 1]
            elif i < n and txt[i] != pat[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return result
