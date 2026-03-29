class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+'#'+s
        return res
    


    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            string_len = int(s[i:j])
            j+=1
            actual_string = s[j: j+string_len]
            res.append(actual_string)
            i=j+string_len
        return res

