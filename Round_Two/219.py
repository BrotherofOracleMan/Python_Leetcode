class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i = 0
        hash_set = set()
        for j in range(len(nums)):
            if(j-i-1) >= k:
                if nums[i] in hash_set:
                    hash_set.remove(nums[i])
                    i+=1
            if i !=j and nums[j] in hash_set:
                    return True
            hash_set.add(nums[j])
        return False
        
