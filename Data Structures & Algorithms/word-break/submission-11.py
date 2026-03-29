class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def f(i):
            if i==len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if i+len(w)<=len(s) and s[i: i+len(w)] == w:

                    if f(i+len(w)):
                        memo[i] = True
                        return True

            memo[i] = False
            return False
        
        f(0)
        print(memo)
        return memo[0]