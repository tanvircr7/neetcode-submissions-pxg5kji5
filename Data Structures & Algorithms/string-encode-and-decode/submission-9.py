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
            len_of_string = int(s[i:j])
            j+=1
            actual_string = s[j:j+len_of_string]
            res.append(actual_string)
            
            i=j+len_of_string
        
        return res