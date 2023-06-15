class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        strings = []
        def backtrack(left, right, curr_string):
            if len(curr_string) == 2 * n:
                print(curr_string)
                strings.append(str("".join(curr_string)))

            if left < n:
                curr_string.append("(")
                backtrack(left +1, right, curr_string)
                curr_string.pop()
            
            if right < left:
                curr_string.append(")")
                backtrack(left, right+1, curr_string)
                curr_string.pop()

        backtrack(0,0,[])
        return strings
