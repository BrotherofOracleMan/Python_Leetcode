class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_par = ["(","{","["]
        closed_bracket_dict = {"{":"}", "[":"]","(":")"}
        for op in s:
            if op in open_par:
                stack.append(op)
            elif len(stack) and op == closed_bracket_dict[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0 
