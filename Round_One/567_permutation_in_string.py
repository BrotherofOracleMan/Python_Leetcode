class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_hashtable = {}
        s2_hashtable = {}
        start = 0
        
        for x in string.ascii_lowercase:
            s1_hashtable[x] = 0
            s2_hashtable[x] = 0
        for word_ch in s1:
            s1_hashtable[word_ch]+=1

        for index,word_ch in enumerate(s2):
            s2_hashtable[word_ch] +=1
            if index - start + 1 == len(s1):
                if s1_hashtable == s2_hashtable:
                    return True
                else:
                    s2_hashtable[s2[start]]-=1
                    start+=1
        return False
        
