class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res = res + str(l) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            size = int(s[i:j])
            j += 1
            res.append(s[j:j+size])
            i = j+size
        
        return res
