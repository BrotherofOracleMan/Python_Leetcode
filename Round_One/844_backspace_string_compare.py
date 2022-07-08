class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_stack = []
        t_stack = []
        
        for char in s:
            if char == '#' and len(s_stack) == 0:
                continue
            elif char == "#":
                s_stack.pop()
            else:
                s_stack.append(char)
                
        for char in t:
            if char == '#' and len(t_stack) == 0:
                continue
            elif char == '#':
                t_stack.pop()
            else:
                t_stack.append(char)
        
        return ''.join(t_stack) == ''.join(s_stack)
