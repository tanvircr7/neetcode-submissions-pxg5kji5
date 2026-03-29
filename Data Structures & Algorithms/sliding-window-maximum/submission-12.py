class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans = []
        l=0
        r=0
        res = []

        dq = deque()

        while r<len(nums):

            while dq and nums[r]>nums[dq[-1]]:
                dq.pop()
            
            dq.append(r)

            if r-l+1 == k:
                res.append(nums[dq[0]])
                l+=1
            
            if l>dq[0]:
                dq.popleft()

            r+=1
        
        return res




            