class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        maxcnt = 0

        for n in nums:
            cnt[n] += 1
            if cnt[n] > maxcnt:
                maxcnt = cnt[n]

                if maxcnt > math.floor(len(nums) / 2):
                    return n

