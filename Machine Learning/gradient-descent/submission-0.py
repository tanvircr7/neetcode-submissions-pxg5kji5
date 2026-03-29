class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        def slope(i):
            return 2*i
        
        curr = init
        for i in range(iterations):
            d = slope(curr)
            curr = curr - (learning_rate*d)
        
        return round(curr, 5)
    