class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        def slope(i):
            return 2*i
        
        for i in range(iterations):
            d = slope(init)
            new_val = init - learning_rate*d
            init = new_val
        
        return round(init, 5)