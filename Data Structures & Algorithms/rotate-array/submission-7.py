class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        n = len(nums)
        count = 0
        startHarness = 0

        while count < n:
            currentIdx = startHarness
            prev_val = nums[startHarness]

            while True:
                next_idx = (currentIdx+k)%n

                nums[next_idx], prev_val = prev_val, nums[next_idx]
                count += 1
                currentIdx = next_idx
                if startHarness == currentIdx:
                    break
            startHarness += 1


