class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        res = []

        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            print(s[i:j])
            num = int(s[i:j])
            start, end = j+1, j+1+num
            stri = s[start: end]
            res.append(stri)
            i = end
        
        return res