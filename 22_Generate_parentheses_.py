class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generateParenthesis_helper(number_left,number_right,number_of_parentheses,list_str,parentheses_list):
            if len(list_str)//2 == number_of_parentheses:
                parentheses_list.append("".join(list_str))
                return
            if number_left < number_of_parentheses:
                list_str.append("(")
                generateParenthesis_helper(number_left+1,number_right,number_of_parentheses,list_str,parentheses_list)
                list_str.pop()
            if number_right < number_left:
                list_str.append(")")
                generateParenthesis_helper(number_left,number_right+1,number_of_parentheses,list_str,parentheses_list)
                list_str.pop()
            
            return
        
        parentheses_list = []
        if n == 0:
            return []
        else:
            generateParenthesis_helper(0,0,n,[],parentheses_list)
            return parentheses_list
