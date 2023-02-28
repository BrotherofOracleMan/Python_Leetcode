class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(0, len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                index = stack[-1][1]
                ans[index] = i - index
                stack.pop()
            stack.append([temperatures[i], i])
        return ans
