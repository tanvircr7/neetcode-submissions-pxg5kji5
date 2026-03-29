class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0 for i in range(len(nums))]
        postfix = [0 for i in range(len(nums))]
        res = []

        prefix[0]=1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        postfix[len(nums)-1]=1
        for i in range(len(nums)-2,-1,-1):
            postfix[i] = postfix[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[i])

        for x in prefix:
            print(x)
        for y in postfix:
            print(y)

        return res
        

        