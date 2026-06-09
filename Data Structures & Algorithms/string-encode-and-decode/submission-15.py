class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            print(f"J -> {j}")
            num = int(s[i:j])
  
            stringtoadd = s[j+1:j+num+1]
            res.append(stringtoadd)
            i=j+num+1
            print(f"i -> {i}")
        
        return res