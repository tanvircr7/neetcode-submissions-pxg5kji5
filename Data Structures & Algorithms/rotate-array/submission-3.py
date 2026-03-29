class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)

        # if gcd(n,k)>1 then you'll need n/gcd(n,k) cycles for the loop

        count = 0      # Total elements moved so far
        start = 0      # Starting index of current cycle

        while count < n:
            current = start
            prev = nums[start]   # Save the starting element

            while True:
                next_idx = (current + k) % n
                # Swap: put 'prev' into its destination, save displaced value
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:  # Completed a full cycle
                    break

            start += 1  