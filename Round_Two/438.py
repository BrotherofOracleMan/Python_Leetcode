from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        sld_win = [0] * 26
        original_hash_table = [0] * 26
        p_len = len(p)

        for i in range(len(p)):
            original_hash_table[ord(p[i]) - ord('a')] +=1

        begin_index = 0
        for end_index in range(len(s)):
            #print(s[end_index])
            sld_win[ord(s[end_index]) - ord('a')] +=1
            if end_index - begin_index + 1 == p_len:
                #print(sld_win)
                if original_hash_table == sld_win:
                    ans.append(begin_index)
                sld_win[ord(s[begin_index])- ord('a')] -=1
                begin_index+=1
        return ans
