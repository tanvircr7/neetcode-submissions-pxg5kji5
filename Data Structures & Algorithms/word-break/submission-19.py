class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def f(i):
            if i==len(s):
                return True
            
            if i in memo:
                return memo[i]

            for w in wordDict:

                if i+len(w) <= len(s) and w == s[i:i+len(w)]:
                    
                    if f(i+len(w)):
                        memo[i] = True

                        return True
                    

            memo[i] = False
            return False
        
        return f(0)