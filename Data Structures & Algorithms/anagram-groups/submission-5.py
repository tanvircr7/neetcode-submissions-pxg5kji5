class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        func = lambda c: ord(c)-ord('a')

        for s in strs:
            cnt = [0 for i in range(26)]

            for c in s:
                cnt[func(c)] += 1
            
            res[tuple(cnt)].append(s)


        return list(res.values())