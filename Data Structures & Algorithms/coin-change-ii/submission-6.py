class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # coins.sort()
        dp = [[-1]*(amount+1) for i in range(len(coins))]

        def f(i, val):
            if val==0:
                return 1
            if i>=len(coins):
                return 0
            
            if dp[i][val] != -1:
                return dp[i][val]
            
            res = f(i+1, val)
            if val-coins[i]>=0:
                res += f(i, val-coins[i])
            
            dp[i][val] = res
            return res
        
        ans = f(0, amount)
        print(dp)
        return ans
