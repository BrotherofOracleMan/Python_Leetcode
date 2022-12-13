class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op1 = 0
        op2 = 0
        for token in tokens:
            if token in ["+","-","*","/"]:
                op2,op1 = int(stack.pop()) , int(stack.pop())
                if token == "+": stack.append(op2 + op1)
                elif token == "-": stack.append(op1 - op2)
                elif token == "*": stack.append(op2 * op1)
                elif token == "/": stack.append(op1/op2)
            else:
                stack.append(token)
        return int(stack[-1])
