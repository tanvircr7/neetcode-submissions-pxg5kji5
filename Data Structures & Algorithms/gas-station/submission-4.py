class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        diff = [gas[i]-cost[i] for i in range(len(gas))]

        i = 0
        startidx = -1
        while i<len(gas)-1:

            if diff[i]>=0:
                if startidx < 0:
                    startidx = i
            
            else:
                startidx = -1
            i += 1
        
        if startidx == -1:
            if diff[len(gas)-1] >=0:
                return len(gas)-1
            else:
                return 0

        return startidx
        

