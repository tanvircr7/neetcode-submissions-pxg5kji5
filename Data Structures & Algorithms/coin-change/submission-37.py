class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = [amount+1]*(amount+1)

        memo[0] = 0

        for v in range(1, amount+1):
            for c in coins:

                if v-c >=0 :
                    memo[v] = min(memo[v], memo[v-c]+1)
        

        return memo[amount] if memo[amount]!=amount+1 else -1

