class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)==0:
            return [[]]

        res = []
        
        perms = self.permute(nums[1:])

        for p in perms:
            for i in range(0, len(p)+1):
                pcopy = p.copy()
                pcopy.insert(i, nums[0])
                res.append(pcopy.copy())
        
        return res


