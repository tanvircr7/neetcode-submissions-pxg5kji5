class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        n=len(nums)
        count = 0
        startHarness = 0

        while count<n:
            curr_idx = startHarness
            prev_val = nums[startHarness]
            while True:
                next_idx = (curr_idx + k) % n

                nums[next_idx], prev_val = prev_val, nums[next_idx]
                count += 1
                curr_idx = next_idx
                if curr_idx == startHarness:
                    break
            startHarness += 1



        

        
        




