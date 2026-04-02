class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(w):
            print(f"-> {w}")
            currSum = 0
            parts = 0
            for n in weights:
                currSum += n
                if currSum > w:
                    print(f"parting at {n}")
                    currSum = n
                    parts += 1
            ship_time = parts + 1
            print(f"time {ship_time}")
            return ship_time <= days
        

        l,r = max(weights), sum(weights)
        ans = sum(weights)+1
        while l<=r:
            w = l+(r-l) // 2
            print(f"{l} - {r}")
            
            if canShip(w):
                ans = w
                r = w-1
            else:
                l = w+1
        
        return ans