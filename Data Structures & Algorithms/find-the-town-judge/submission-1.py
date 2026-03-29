class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0]*(n+1)
        itrust = [0]*(n+1)

        for a,b in trust:
            itrust[a] += 1
            trusted[b] += 1

        ans = []
        
        for i in range(1,n+1):
            if itrust[i]==0 and trusted[i]==n-1:
                ans.append(i)
        
        return ans[0] if len(ans)==1 else -1
