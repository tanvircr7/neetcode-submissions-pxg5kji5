class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        idx = len(profit)-1
        return self.f(capacity, profit, weight, idx)

    def f(self, cap, p, w, idx):
        if idx <0 or cap==0:
            return 0
        
        take = 0
        take_again = 0
        if cap-w[idx]>=0:
            take = self.f(cap-w[idx], p, w, idx-1) + p[idx]
            take_again = self.f(cap-w[idx], p, w, idx) + p[idx]
     
        take_not = self.f(cap, p, w, idx-1)

        return max(take, take_again, take_not)