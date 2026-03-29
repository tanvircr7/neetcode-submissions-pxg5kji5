class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        sz = len(s)
        if sz%2 == 0:
            offset = 0
            for i in range(0,sz//2):
                s[i], s[sz-1-i] = s[sz-1-i], s[i]
        
        else:
            for i in range(0, sz//2):
                s[i], s[sz-1-i] = s[sz-1-i], s[i]
        