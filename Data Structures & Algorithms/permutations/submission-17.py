class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)==0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(0, len(p)+1):
                cpy = p.copy()
                cpy.insert(i, nums[0])
                res.append(cpy)
        
        return res