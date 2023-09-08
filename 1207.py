from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h_t = defaultdict(int)
        set_check = set()

        for val in arr:
            h_t[val] += 1

        for val in h_t.values():
            if val in set_check:
                return False
            set_check.add(val)

        return True
