class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "$" + s[:]
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            j = i
            while s[j] != "$":
                j += 1
            
            number = int(s[i:j])
            j+=1

            decodedString = s[j:j+number]

            res.append(decodedString)

            i = j+number

        return res
            
