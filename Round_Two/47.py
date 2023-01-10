from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, Counter):
            if len(comb) == len(nums):
                results.append(list(comb))
            
            for key in Counter:
                if Counter[key] > 0:
                    comb.append(key)
                    Counter[key] -= 1
                    backtrack(comb, Counter)
                    Counter[key] += 1
                    comb.pop()
        counter_dict = Counter(nums)
        backtrack([], counter_dict)
        return results
