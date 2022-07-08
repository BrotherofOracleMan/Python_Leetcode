class Solution(object):
    def __init__(self):
        self.result = []
    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtrack(string, current_list,start):
            if len(current_list) == 4:
                if start == len(string):
                    self.result.append(".".join(current_list))
                else:
                    return
            
            for i in range(start,min(start + 3, len(string))):
                if string[start] == '0' and i > start:
                    continue
                if  int(string[start:i+1]) >= 0 and int(string[start:i+1]) <= 255:
                    current_list.append(string[start:i+1])
                    backtrack(string,current_list,i+1)
                    current_list.pop()
                    
        backtrack(s,[],0)
        return self.result