from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_good_pairs = 0
        h_t = defaultdict(list)

        for index,value in enumerate(nums):
            h_t[value].append(index)

        for index,value in enumerate(nums):
            list_nums = h_t[value]
            for indice in list_nums:
                if indice > index:
                    num_good_pairs +=1 

        return num_good_pairs
