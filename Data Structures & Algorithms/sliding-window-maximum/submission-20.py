class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        l=0
        ans = []
        r = 0

        while r<len(nums):

            while q and nums[q[-1]]<nums[r]:
                q.pop()
            
            q.append(r)

            if r-l+1 == k:
                ans.append(nums[q[0]])
                l+=1
            
            if q[0] < l:
                q.popleft()

            r+=1

        return ans
            