class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        GG = amount+1
        memo = [GG]*GG
        memo[0] = 0
        
        for v in range(1, amount+1):
            for c in coins:
                if v-c >= 0:
                    memo[v] = min(memo[v], memo[v-c]+1)

        ans = memo[amount]

        return ans if ans != GG else -1


