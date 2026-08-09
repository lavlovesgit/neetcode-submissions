class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        s = 0
        c = 0
        minc = float('inf')
        R = 0

        while R < len(nums):
            while R < len(nums) and s < target:
                s += nums[R]
                c += 1
                R += 1

            while s >= target:
                minc = min(minc, c)
                s -= nums[L]
                c -= 1
                L += 1

        return 0 if minc == float('inf') else minc