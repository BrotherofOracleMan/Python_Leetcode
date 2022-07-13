class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hash_table_s1 = [0] * 26
        hash_table_s2 = [0] * 26
        for c in s1:
            hash_table_s1[ord(c) - ord('a')] +=1
        i=0
        for j in range(len(s2)):
            hash_table_s2[ord(s2[j])-ord('a')] += 1
            if (j - i + 1) > len(s1):
                hash_table_s2[ord(s2[i])-ord('a')] -=1
                i += 1
            if j -i + 1 == len(s1):
                if hash_table_s2 == hash_table_s1:
                    return True
        return False
        
