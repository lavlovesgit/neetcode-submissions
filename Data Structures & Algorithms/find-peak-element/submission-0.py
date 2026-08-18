class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
            n = len(nums)

            if n == 1:
                return 0

            if nums[0] > nums[1]:
                return 0

            p = 2

            while p < n:
                if nums[p] < nums[p-1] and nums[p-2] < nums[p-1]:
                    return p-1

                p += 1

            return n - 1
            