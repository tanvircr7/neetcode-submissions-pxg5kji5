class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            strlen = int(s[i:j])
            print(strlen)

            j+=1
            tmpstr = s[j:j+strlen]
            
            res.append(tmpstr)

            i = j+strlen
        
        return res