class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        f = lambda c: ord(c)-ord('a')

        for s in strs:
            index = [0]*26

            for c in s:
                index[f(c)]+=1
            
            res[tuple(index)].append(s)

        return list(res.values())
