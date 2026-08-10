class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)

        res = []

        for p,s in pair:

            time = (target-p)/s

            if len(res)==0:
                res.append([time,1])
                continue

            if time <= res[-1][0]:
                res[-1][1] += 1
            else:
                res.append([time, 1])
            # print(res)
        
        return len(res)
            
            

