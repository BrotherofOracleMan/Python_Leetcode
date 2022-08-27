class Solution:
    def romanToInt(self, s: str) -> int:
        int_sum = 0
        i = 0
        hash_table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        while i < len(s):
            if len(s) - i >= 2 and hash_table[s[i+1]] > hash_table[s[i]]:
                int_sum += (hash_table[s[i+1]] - hash_table[s[i]])
                i+=2
            else:
                int_sum += hash_table[s[i]]
                i+=1

        return int_sum
