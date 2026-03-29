class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        func = lambda k: ord(k)-ord('a')

        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[func(c)] += 1
            
            res[tuple(cnt)].append(s)
        
        print(res.values())
        return list(res.values())