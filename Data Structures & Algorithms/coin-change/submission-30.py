class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount+1]*(amount+1)

        memo[0] = 0

        print(memo)

        for val in range(1, amount+1):
            for c in coins:

                if val-c >= 0:
                    memo[val] = min(memo[val], memo[val-c]+1)

        return memo[amount] if memo[amount]!=amount+1 else -1

            
            


