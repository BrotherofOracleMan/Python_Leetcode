class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def lettercombhelper(current_comb, num_map, number_counter, len_numbers,ans):
            if number_counter == len_numbers:
                ans.append(str(current_comb))
                return

            for character in num_map[digits[number_counter]]:
                lettercombhelper(current_comb + character, num_map, number_counter + 1, len_numbers, ans)
        ans = []
        num_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        if digits == "":
            return []
        lettercombhelper("", num_map,0,len(digits),ans)
        return ans
