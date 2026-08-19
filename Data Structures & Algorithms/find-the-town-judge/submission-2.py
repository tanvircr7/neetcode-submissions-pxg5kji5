class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = -1
        cnt = {i:[0,0] for i in range(1, n+1)}

        for x,y in trust:
            cnt[x][1] += 1
            cnt[y][0] += 1
        
        for i in range(1, n+1):
            if cnt[i][0] == n-1 and cnt[i][1] == 0:
                return i
        
        return -1