class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        perm=[]
        def rec():
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            for num in nums:
                if num in perm:
                    continue
                perm.append(num)
                rec()
                perm.pop()
        rec()
        return res

        