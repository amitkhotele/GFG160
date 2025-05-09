class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        result = set()
        pair_sum_map = {}

        for i in range(n):
            for j in range(i + 1, n):
                pair_sum = arr[i] + arr[j]
                if pair_sum not in pair_sum_map:
                    pair_sum_map[pair_sum] = []
                pair_sum_map[pair_sum].append((i, j))

        for i in range(n):
            target = -arr[i]
            if target in pair_sum_map:
                for pair in pair_sum_map[target]:
                    if i not in pair:
                        triplet = tuple(sorted([i, pair[0], pair[1]]))
                        result.add(triplet)

        return sorted([list(triplet) for triplet in result])
      
