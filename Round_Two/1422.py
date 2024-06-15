class Solution:
    def maxScore(self, s: str) -> int:
        number_of_zeros = 0
        number_of_ones = [0] * len(s)
        max_score = float("-inf")
        ones_counter = 0

        for index in range(len(s)):
            if s[index] == '1':
                ones_counter += 1
            number_of_ones[index] = ones_counter
        
        for i in range(len(s) -1):
            if s[i] == '0':
                number_of_zeros += 1
            max_score = max(max_score, number_of_zeros + (number_of_ones[-1] - number_of_ones[i]))
        return max_score
