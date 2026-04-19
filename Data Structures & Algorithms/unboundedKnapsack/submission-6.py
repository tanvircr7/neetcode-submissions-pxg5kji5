class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        R, C = len(weight), capacity+1
        memo = [[-1]*(C) for i in range(R)]

        return self.kp(0, capacity, profit, weight, memo)

    def kp(self, i, cap, p, w, memo):
        if i==len(p):
            return 0
        
        if memo[i][cap] != -1:
            return memo[i][cap]
        
        res = 0
        notake = self.kp(i+1, cap, p, w, memo)
        take = 0
        if w[i] <= cap:
            take = self.kp(i, cap-w[i], p, w, memo)+p[i]

        res = max(notake, take)

        memo[i][cap] = res
        return res