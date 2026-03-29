class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        sz = len(s)


        for i in range(sz//2):
            s[i], s[-1-i] = s[-1-i], s[i]

        return s

        
        