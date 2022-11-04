class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def parse(stack,string):
            for char in string:
                if char == "#":
                    if len(stack):
                        stack.pop()
                else:
                    stack.append(char)
            print(stack)
            return stack
        
        return parse([],s) == parse([], t)
