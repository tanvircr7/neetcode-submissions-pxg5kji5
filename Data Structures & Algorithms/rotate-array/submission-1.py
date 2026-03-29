class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        n = len(nums)

        count = 0
        start_harness = 0

        while count < n:
            current = start_harness
            prev = nums[start_harness]

            while True:
                next_idx = (current+k)%n
                nums[next_idx], prev = prev, nums[next_idx]
                count += 1
                current = next_idx

                if start_harness == current:
                    break
            
            start_harness += 1