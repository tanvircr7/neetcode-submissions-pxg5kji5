class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def f(i, currstr):
            # base case
            if i==len(digits):
                res.append(currstr)
                return 

            chars = digitToChar[digits[i]]
            for c in chars:
                f(i+1, currstr+c)
            
            return

        f(0, "")
        return res
            





