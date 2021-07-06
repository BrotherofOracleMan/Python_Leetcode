from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_table = defaultdict(list)
        listoflists = []
        
        for string in strs:
            hash_table["".join(sorted(string))].append(string)
            
        return hash_table.values()
        
        
