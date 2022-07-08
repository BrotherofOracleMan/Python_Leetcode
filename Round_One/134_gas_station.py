class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0
        total_gas , current_gas  = 0 , 0
        
        for i in range(len(gas)):
            total_gas += (gas[i] - cost[i])
            current_gas += (gas[i] - cost[i])
            if current_gas <0:
                start = i + 1
                current_gas = 0
        return start if total_gas >= 0 else -1
