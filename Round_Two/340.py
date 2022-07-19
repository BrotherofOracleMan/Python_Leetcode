class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        
        if n == 0 or k == 0:
            return 0
        
        i = 0
        hashmap = OrderedDict()
        max_res = 1
        for j in range(n):
            if s[j] in hashmap:
                del hashmap[s[j]]
            hashmap[s[j]] = j
            if len(hashmap) ==(k+1):
                _ , del_idx = hashmap.popitem(last= False)
                i = del_idx +1
            max_res = max(max_res, j - i + 1)
        return max_res
        
        """
        hash_table = [0] * 128
        hash_set = set()
        i = 0
        max_res = -1
        for j in range(len(s)):
            hash_set.add(s[j])
            hash_table[ord(s[j])-ord('a')] += 1
            while len(hash_set) > k:
                hash_table[ord(s[i])-ord('a')] -= 1
                if hash_table[ord(s[i])-ord('a')] == 0:
                    hash_set.remove(s[i])
                i+=1
            max_res = max(j-i+1, max_res)
        return max_res
        """ 
        
