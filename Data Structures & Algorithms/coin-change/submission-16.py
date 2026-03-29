class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def f(val):
            if val==0:
                return 0
            
            if val in memo:
                return memo[val]

            tmp = 1e9
            for c in coins:
                if val-c >= 0:
                    tmp = min(tmp, f(val-c)+1)

            memo[val] = tmp
            return tmp


        val = f(amount)

        return val if val!=1e9 else -1