class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q = deque([0])
        reach = [False]*len(nums)

        while q:
            u = q.popleft()
            reach[u] = True

            for i in range(nums[u]+1):
                if u+i < len(nums) and reach[u+i]==False:
                    q.append(u+i)
            
        
        if reach[len(nums)-1]:
            return True
        else:
            return False