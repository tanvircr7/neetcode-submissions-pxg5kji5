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
            num = int(s[i:j])
            j+=1
            val = s[j:j+num]
            res.append(val)
            i = j+num

        return res