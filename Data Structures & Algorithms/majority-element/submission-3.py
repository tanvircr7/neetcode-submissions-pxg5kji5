class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {n: 0 for n in nums}
        majcnt = 0
        res = -1
        elements = len(nums)

        for n in nums:
            cnt[n] += 1

            if cnt[n] > majcnt:
                majcnt = cnt[n]
                res = n

                if majcnt > math.floor(elements/2):
                    return res

        return res

