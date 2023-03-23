from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        ans = []
        for string in strs:
            ht[''.join(sorted(string))].append(string) 
        
        return ht.values()
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for s in string:
                count[ord(s) - ord('a')] += 1
            ht[tuple(count)].append(string)
        return ht.values()

"""
