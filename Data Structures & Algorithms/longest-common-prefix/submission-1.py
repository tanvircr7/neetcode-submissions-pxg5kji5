class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        limit = min(len(s) for s in strs)

        flag = 0
        k = 1
        for i in range(0,limit):
            k=1
            match = strs[0][i]
            for j in range(1, len(strs)):
                if match == strs[j][i]:
                    k+=1
                else:
                    break
            
            if k==len(strs):
                flag += 1
            else:
                break
        

        return strs[0][:flag]
            
