class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            c = s[i]

            if c!="]":
                stk.append(c)
            else:
                substr = ""
                while stk and stk[-1]!="[":
                    substr = stk.pop() + substr
                stk.pop()

                k = ""
                while stk and stk[-1].isdigit()==True:
                    digit = stk.pop()
                    k = digit + k
                val = int(k)*substr
                stk.append(val)
        
        return "".join(stk)