class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        gas_tank = 0
        start= 0
        for i in range(0,len(cost)):
            total_gas += (gas[i] - cost[i])
            gas_tank += (gas[i] - cost[i])
            if gas_tank < 0:
                start = i + 1
                gas_tank = 0
        return start if total_gas >= 0 else -1

        """
        n = len(cost)

        for i in range(n):
            remaining_gas = 0
            cycle = 0
            for j in range(n):
                k = (i +j) % n
                remaining_gas += (gas[k] - cost[k])
                if remaining_gas < 0:
                    break
                cycle +=1
            if n == cycle:
                return i
        return -1
        """
