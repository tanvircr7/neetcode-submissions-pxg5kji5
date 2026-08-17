class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0

        def h():
            k = 0
            res = ""

            while self.i < len(s):
                c = s[self.i]

                if c.isdigit():
                    k = k*10 + int(c)
                elif c=="[":
                    self.i += 1
                    res = res + k*h()
                    k = 0
                elif c=="]":
                    return res
                else:
                    res = res + c
                
                self.i += 1
            
            return res
        
        return h()