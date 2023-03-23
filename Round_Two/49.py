from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        ans = []
        for string in strs:
            ht[''.join(sorted(string))].append(string) 
        
        return ht.values()
