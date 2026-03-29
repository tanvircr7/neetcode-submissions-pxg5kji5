class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ans = 0
        tmp = 0
        cnt = {}

        for r in range(len(s)):
            c = s[r]
            cnt[c] = cnt.get(c,0)+1

            while cnt[c]>1:
                a = s[l]
                cnt[a] -= 1
                l+=1
            
            ans = max(ans, r-l+1)
        
        return ans