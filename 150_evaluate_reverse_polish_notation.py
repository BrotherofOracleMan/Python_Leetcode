class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rpn_stack = []
        
        for i in range(len(tokens)):
            if tokens[i].isnumeric() or tokens[i].strip('-').isnumeric():
                tokens[i] = int(tokens[i])
        
        
        for token in tokens:
            if token == '+':
                op2 = rpn_stack.pop()
                op1 = rpn_stack.pop()
                rpn_stack.append(op1+op2)
            elif token == '-':
                op2 = rpn_stack.pop()
                op1 = rpn_stack.pop()
                rpn_stack.append(op1 - op2)
            elif token == "*":
                op2 = rpn_stack.pop()
                op1 = rpn_stack.pop()
                rpn_stack.append(op1 * op2)
            elif token == "/":
                op2 = rpn_stack.pop()
                op1 = rpn_stack.pop()
                rpn_stack.append(int(op1/op2))
            else:
                rpn_stack.append(token)
                
        return rpn_stack.pop()
        
        
