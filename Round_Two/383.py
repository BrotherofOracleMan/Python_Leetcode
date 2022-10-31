 from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_ht = defaultdict(int)
        magazine_ht = defaultdict(int)

        for char_r in ransomNote:
            ransomNote_ht[char_r] += 1

        for char_m in magazine:
            magazine_ht[char_m] +=1
        
        for entry in ransomNote_ht.keys():
            if entry not in magazine_ht or ransomNote_ht[entry] > magazine_ht[entry]:
                return False
        return True
