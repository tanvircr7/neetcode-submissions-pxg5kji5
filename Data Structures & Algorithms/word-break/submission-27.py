class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def f(i):
            print(f"{i} < _ > {len(s)}")
            if i==len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                print(f" - {w} -- ")
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:

                    print(f"at {i} -> {w}")
                    if f(i+len(w)):
                        print("success")
                        memo[i] = True
                        return True
                    
            
            memo[i] = False
            return False
        
        return f(0)