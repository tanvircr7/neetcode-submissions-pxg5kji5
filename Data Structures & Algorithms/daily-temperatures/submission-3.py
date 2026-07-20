class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stk = deque()
        stk.append([temperatures[0], 0])
        
        for i in range(1, len(temperatures)):
            t = temperatures[i]
            print(f"for -- {i} - {t}")
            while stk and t>stk[-1][0]:
                val, idx = stk.pop()
                print(f"{val} - {idx}")
                res[idx] = i-idx
            
            stk.append([t,i])
        
        return res