class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()


        memo = {}

        def f(i, val):
            if val == 0:
                return 1
            if i==len(coins):
                return 0
            
            if (i,val) in memo:
                return memo[(i,val)]
            
            res = 0
            notake = f(i+1, val)
            take = 0
            if val-coins[i] >= 0:
                take = f(i, val-coins[i])
            
            res = take + notake
            memo[(i,val)] = res
            return res
        
        ans = f(0, amount)

        return ans
