class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p,s) for p,s in zip(position, speed)]

        pair.sort(reverse=True)

        stack = []


        for p,s in pair:

            stack.append( (target-p) / s )

            # stack[-2] being greater means the time is greater ..
            # the time being greater means it's slower
            # so the car behind merges the fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
        
