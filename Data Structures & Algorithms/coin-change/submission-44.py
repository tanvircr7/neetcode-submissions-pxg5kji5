class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        GG = amount+1
        memo = [GG]*GG
        memo[0] = 0

        for val in range(amount+1):
            for c in coins:

                if val-c >= 0:
                    memo[val] = min(memo[val], memo[val-c]+1)
        
        ans = memo[amount]

        return ans if ans != GG else -1