class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hourHand = (hour%12.0) * 30.0 + float(minutes/60.0) * 30.0
        minuteHand = minutes * 6.0
        
        if minuteHand > hourHand:
            differenceOne = (360 - minuteHand) + hourHand
            differenceTwo = minuteHand - hourHand
            return min(differenceOne, differenceTwo)
        else:
            differenceOne = (360 - hourHand) + minuteHand
            differenceTwo = hourHand - minuteHand
            return min(differenceOne, differenceTwo)
