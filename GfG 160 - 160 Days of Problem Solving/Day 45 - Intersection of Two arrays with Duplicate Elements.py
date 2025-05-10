class Solution:
    def intersectionWithDuplicates(self, a, b):
        set_a = set(a)
        result = []

        for num in b:
            if num in set_a:
                result.append(num)
                set_a.remove(num)

        return result
