class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            num = int(s[i:j])
            start = j+1
            end = j+1+num
            stringtoadd = s[start:end]
            res.append(stringtoadd)

            i = end
        
        return res