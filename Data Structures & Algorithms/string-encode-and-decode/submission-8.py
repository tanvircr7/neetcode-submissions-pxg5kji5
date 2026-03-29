class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res
    


    def decode(self, s: str) -> List[str]:
        res = []
        
        i=0
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            num = s[i:j]
            num = int(num)
            j+=1
            extract = s[j:j+num]
            res.append(extract)

            i = j+num

        return res