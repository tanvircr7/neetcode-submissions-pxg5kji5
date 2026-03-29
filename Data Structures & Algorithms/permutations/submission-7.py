class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)==0:
            return [[]]
        
        perms = self.permute(nums[1:])

        res = []
        print(perms)
        for p in perms:
            for i in range(0, len(p)+1):
                c = p.copy()
                c.insert(i, nums[0])
                res.append(c)
        
        return res


