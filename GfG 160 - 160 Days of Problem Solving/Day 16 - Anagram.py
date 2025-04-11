class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False

        counts = [0] * 26
        for i in range(len(s1)):
            counts[ord(s1[i]) - ord('a')] += 1
            counts[ord(s2[i]) - ord('a')] -= 1

        for count in counts:
            if count != 0:
                return False

        return True
