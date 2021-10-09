class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        letter_stack = []
        l = 0
        string = ""
        
        for letter in s:
            if not letter_stack or letter_stack[-1][0] != letter:
                letter_stack.append([letter,1])
            elif letter_stack[-1][0] == letter:
                letter_stack[-1][1] +=1
            if letter_stack[-1][1] == k:
                letter_stack.pop()
        
        for pair in letter_stack:
            string += pair[0] * pair[1] 
        
        
        return string
        
        
        