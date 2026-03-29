class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        idx = 0

        diff = [gas[i]-cost[i] for i in range(len(gas))]

        if sum(diff) < 0:
            return -1

        for i, n in enumerate(diff):
            total += n

            if total<0:
                idx = i + 1
                total = 0

        return idx