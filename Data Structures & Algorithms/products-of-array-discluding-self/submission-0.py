from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prod = 1
            else:
                prod = prod * nums[i - 1]
                pre[i] = prod

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                prod = 1
            else:
                prod = prod * nums[i + 1]
                post[i] = prod

        for i in range(len(nums)):
            post[i] = post[i] * pre[i]

        return post