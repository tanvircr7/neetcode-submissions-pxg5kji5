class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        sz = len(s)//2
        n = len(s)-1

        for i in range(0, sz):
            s[i], s[n-i] = s[n-i], s[i]

        
        