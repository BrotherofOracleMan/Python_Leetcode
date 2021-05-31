class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashtable = {}
        start = 0
        longest_value = 0
        for index,word_ch in enumerate(s):
            if hashtable.get(word_ch) is None:
                hashtable[word_ch] = 0
            hashtable[word_ch]+=1
            if hashtable.get(word_ch) > 1:
                hashtable[s[start]]-=1
                start+=1
            for key,value in hashtable.items():
                if value > 1:
                    hashtable[s[start]] -= 1
                    start+=1
            longest_value = max(longest_value,index-start + 1)
        return longest_value
                
           
