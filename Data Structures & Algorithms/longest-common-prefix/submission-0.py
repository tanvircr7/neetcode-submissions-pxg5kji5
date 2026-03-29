class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n= len(strs)

        res = ""

        minx = min(len(strs[i]) for i in range(len(strs)))

        x = minx
        cnt = 0
        for j in range(0,x):
            curr = strs[0][j]
            print(f"Curr {curr}")
            for i in range(len(strs)):
                if strs[i][j] != curr:
                    return res
                cnt += 1
                if cnt >= len(strs):
                    res = res + strs[0][j]
                    cnt = 0
                    break
        
        return res