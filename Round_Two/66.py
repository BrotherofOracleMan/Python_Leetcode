class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        carryover  = 0
        if digits[-1] < 10:
            return digits
        else:
            digits[-1] = 0
            carryover = 1

        for i in range(len(digits)-2,-1, -1):
            if carryover:
                if digits[i] + carryover > 9:
                    digits[i] = 0
                    carryover = 1
                else:
                    digits[i] = digits[i] + carryover
                    carryover = 0
                    
        if carryover:
            return [1] + digits
        return digits
