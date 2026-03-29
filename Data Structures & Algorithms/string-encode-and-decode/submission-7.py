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
            j=i
            while s[j]!="#":
                j+=1
            num = int(s[i:j])
            print(num)
            j+=1
            str_to_add = s[j:j+num]
            print(str_to_add)
            res.append(str_to_add)

            i=j+num
        
        return res