class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        hm={}
        maxnum=0
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

            if hm[num]>n/2:
                maxnum=num

        return maxnum


        