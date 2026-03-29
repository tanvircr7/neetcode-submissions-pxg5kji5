class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        return self.dfs(0, capacity, profit, weight)
    
    def dfs(self, i, left, p, w):
        if left == 0:
            return 0
        
        if i>=len(p):
            return 0
        
        res = -1
        if left-w[i]>=0:
            res = max(res, p[i]+self.dfs(i+1, left-w[i], p, w))
        
        res = max(res, self.dfs(i+1, left, p, w))

        return res
    
