class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        mincost0 = [-1]*(len(cost)+1)
        mincost1 = [-1]*(len(cost)+1)


        def f(i,w):
            if i==len(cost):
                return 0
            if i>len(cost):
                return 0
            
            if w[i] != -1:
                return w[i]
            
            res = min(f(i+1,w), f(i+2,w)) + cost[i]
            w[i] = res
            return res
        
        v1 = f(0, mincost0)
        v2 = f(1, mincost1)

        print(mincost0)
        print(mincost1)

        return min(v1,v2)