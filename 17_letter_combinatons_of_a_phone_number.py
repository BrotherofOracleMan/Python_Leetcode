class Solution(object):
    
    
   
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_combinations = []
        current_str = []
        number_letter_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def letterCombinationsHelper(current_str, orig_string, orig_string_index,list_of_strings):
            if orig_string_index == len(orig_string):
                list_of_strings.append("".join(current_str))
                return
            
            for value in number_letter_map[orig_string[orig_string_index]]:
                current_str.append(value)
                letterCombinationsHelper(current_str,orig_string,orig_string_index+1,list_of_strings)
                current_str.pop()
            
            return
        
        if digits == "":
            return ""
        else:
            letterCombinationsHelper(current_str,digits,0,letter_combinations)
        
        return letter_combinations
