class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gas_cycle = gas + gas
        cost_cycle  = cost + cost
        for start in range(len(gas)):
            gas_tank = gas_cycle[start]
            for i in range(len(gas_cycle)):
                if cost_cycle[start + i] > gas_tank:
                    break
                else:
                    if i == len(gas) - 1:
                        return start
                    else:
                        gas_tank = gas_tank - cost_cycle[start + i]
                    gas_tank = gas_tank + gas_cycle[start + i + 1]
        return -1
