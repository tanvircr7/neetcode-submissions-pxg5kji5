class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        memo = [[-1]*(amount+1) for _ in range(len(coins))]

        def dfs(i,a):
            if a==0:
                return 1
            
            if i>=len(coins):
                return 0

            if memo[i][a] != -1:
                return memo[i][a]
            
            res = 0
            if a>=coins[i]:
                notake = dfs(i+1, a)
                take = dfs(i, a-coins[i])
                res = take + notake
            
            memo[i][a] = res
            return res
        
        val = dfs(0, amount)
        print(memo)
        return val