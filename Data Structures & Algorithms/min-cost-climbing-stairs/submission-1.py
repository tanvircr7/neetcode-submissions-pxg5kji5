class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        r = [0,0]

        for i in range(2,len(cost)+1):
            r.append(min(r[i-1]+cost[i-1], r[i-2]+cost[i-2]))
        
        return r[len(cost)]