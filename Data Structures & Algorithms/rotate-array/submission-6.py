class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k%len(nums)
        n = len(nums)
        
        count = 0
        start = 0

        while count < n:
            current = start
            prev = nums[start]

            while True:
                next_idx = (current + k) % n

                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                if start == current:
                    break
            start += 1


