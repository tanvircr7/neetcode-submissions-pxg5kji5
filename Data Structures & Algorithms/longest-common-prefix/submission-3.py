class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        while True:
            if i==len(strs[0]):
                break

            prev = strs[0][i] 
            print(f"harness {prev}")
            for j in range(1, len(strs)):
                if i==len(strs[j]):
                    return strs[0][0:i]
                if strs[j][i] != prev:
                    print(f"break {strs[j]} at {i}")
                    return strs[0][0:i]
            i+=1
        
        return strs[0][0:i]