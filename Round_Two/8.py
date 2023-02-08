class Solution:
    def myAtoi(self, s: str) -> int:

        ans = 0
        index = 0
        nsign = False
        s = s.strip()
        
        if s == "":
            return 0

        INT_MIN = -2**31
        INT_MAX = 2** 31 -1

        if s[0] == '-' or s[0] =='+':
            nsign = True if s[0] == '-' else False
            index+=1

        for i in range(index,len(s)):
            if s[i].isnumeric():
                if((ans > INT_MAX // 10) or (ans== INT_MAX // 10 and int(s[i]) > INT_MAX % 10)):
                    return INT_MAX if not nsign else INT_MIN
                ans = ans * 10 + (ord(s[i]) - ord('0'))
            else:
                break
        return ans * -1 if nsign else ans
