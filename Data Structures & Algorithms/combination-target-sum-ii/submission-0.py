class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # numset = set()
        # num = []
        # for c in candidates:
        #     numset.add(c)
        # for n in numset:
        #     num.append(n)
        num = candidates
        num.sort()
        
        ans = []
        subset = []
        
        def dp(i,val):
            if val == 0:
                ans.append(subset.copy())
                return 
                
            if i>=len(num):
                return
            
            # take
            if val-num[i] >= 0:
                subset.append(num[i])
                dp(i+1, val-num[i])
                subset.pop()
            while i+1 < len(num) and num[i] == num[i+1]:
                i += 1
            # not take
            dp(i+1, val)


        dp(0, target)
        return ans
