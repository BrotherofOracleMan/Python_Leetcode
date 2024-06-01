class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammic_dict = {"1":"1", "9":"6", "6":"9", "8":"8", "0":"0"}
        numcpy = []
        for character in reversed(num):
            if character not in strobogrammic_dict:
                return False
            numcpy.append(strobogrammic_dict[character])
        return "".join(numcpy) == num
        
