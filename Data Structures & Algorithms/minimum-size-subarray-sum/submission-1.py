class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        res=1000000
        curr = 0

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                res = min(res, r-l+1)
                print(f"{curr} at i {r}- val {nums[r]}")
                curr -= nums[l]
                l+=1
            print(f"reset {curr}")
            
        
        return res if res!=1000000 else 0