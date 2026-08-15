class Solution:
    def sortColors(self, nums: List[int]) -> None:
        hm = {}

        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1

        index = 0

        if 0 in hm:
            for i in range(hm[0]):
                nums[index] = 0
                index += 1

        if 1 in hm:
            for i in range(hm[1]):
                nums[index] = 1
                index += 1

        if 2 in hm:
            for i in range(hm[2]):
                nums[index] = 2
                index += 1