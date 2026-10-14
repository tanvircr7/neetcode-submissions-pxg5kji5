class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        cnt = set()
        for n in nums:
            cnt.add(n)
            
        res = 1

        for i in range(len(nums)):
            v = nums[i]

            if v-1 not in cnt:
                tmp = 1
                x = v+1
                while x in cnt:
                    tmp += 1
                    x += 1
                res = max(res, tmp)
        
        return res


