class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        memo = [[-1]*(amount+1) for _ in range(len(coins))]

        def f(i, val):
            if val==0:
                return 1
            if i>=len(coins):
                return 0
            
            if memo[i][val] != -1:
                return memo[i][val]
                
            res =0
            if val-coins[i]>=0:
                res = f(i, val-coins[i])
            res += f(i+1,val)

            memo[i][val] = res
            return res
        
        return f(0, amount)