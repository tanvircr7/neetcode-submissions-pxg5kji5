class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount+1]*(amount+1)
        memo[0] = 0
        
        for i in range(1, amount+1):
            
            for c in coins:

                if i-c >= 0:

                    memo[i] = min(memo[i], memo[i-c]+1)

        
        ans = memo[amount]
        return ans if ans!=(amount+1) else -1
            
            


