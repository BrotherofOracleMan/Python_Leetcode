class Solution:
    def reverseWords(self, s: str) -> str:
        string_list = s.split()
        for i in range(len(string_list)):
            string_list[i] = string_list[i][::-1]
        return " ".join(string_list)
        
