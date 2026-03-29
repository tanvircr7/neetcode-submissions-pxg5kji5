class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            size = len(s)
            res += str(size)+'#'+s[:]
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            j = i
            while s[j]!='#':
                j+=1
            
            size = int(s[i:j])
            j += 1
            tmp = s[j:j+size]
            res.append(tmp)
            i = j+size
        
        return res

