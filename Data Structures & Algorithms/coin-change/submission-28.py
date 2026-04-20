class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for i in range(amount+1):
            
            for j in range(len(coins)):
                c = coins[j]
                
                if i-c >= 0:
                    print(f" i {i} - c {c}")
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        print(dp)
        return dp[amount] if dp[amount] < (amount+1) else -1

            
            


