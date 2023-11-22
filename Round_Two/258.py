
    def getDigtsSum(self, num):
        val_sum  = 0
        while num > 0:
            val_sum += num%10
            num = num // 10
        return val_sum

    def addDigits(self, num: int) -> int:
        while num > 9:
            num = self.getDigtsSum(num)
        return num
