class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        postfix = [0]*len(nums)
        prefix[0]=postfix[len(nums)-1]=1
        for i in range(1, len(prefix)):
            prefix[i] = nums[i-1]*prefix[i-1]
        for i in range(len(postfix)-2, -1, -1):
            postfix[i] = nums[i+1]*postfix[i+1]
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i]*postfix[i])
        return ans
