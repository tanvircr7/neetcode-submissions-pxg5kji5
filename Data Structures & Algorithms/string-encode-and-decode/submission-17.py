class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "@" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i= 0

        while i<len(s):
            j= i
            while s[j] != "@":
                j+=1
            
            num = int(s[i:j])
            start = j+1
            end = j+1+num
            strtopush = s[start: end]

            res.append(strtopush)
            i = j+1+num
        
        return res