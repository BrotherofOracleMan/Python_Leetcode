class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        sol_set = set()
        
        for elem in nums2:
            if elem in set1:
                sol_set.add(elem)

        return list(sol_set)
