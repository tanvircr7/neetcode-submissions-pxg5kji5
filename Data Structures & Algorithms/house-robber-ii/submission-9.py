class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        def driver(arr):
            cost = [-1]*len(arr)

            def f(i):
                if i>=len(arr):
                    return 0
                
                if cost[i] != -1:
                    return cost[i]
                
                nosteal = f(i+1)
                steal = f(i+2)+arr[i]

                res = max(nosteal, steal)
                cost[i] = res
                return res

            return f(0)


        v1 = driver(nums[0: len(nums)-1])
        v2 = driver(nums[1:])

        return max(v1, v2)