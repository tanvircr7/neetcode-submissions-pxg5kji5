class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost0 = [-1]*(len(cost)+1)
        mincost1 = [-1]*(len(cost)+1)


        def f(i, w):
            if i==len(cost):
                return 0
            
            if i>len(cost):
                return 50000

            if w[i]!=-1:
                return w[i]
            
            w[i] = min( f(i+1, w), f(i+2, w)) + cost[i]

            return w[i]

        v1 = f(0, mincost0)
        v2 = f(1, mincost1)

        return min(v1, v2)