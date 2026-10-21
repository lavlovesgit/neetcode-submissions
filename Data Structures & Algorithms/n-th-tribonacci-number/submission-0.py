class Solution:
    def tribonacci(self, n: int) -> int:
        def tri(n,memo):
            if n in memo:
                return memo[n]
            if n==0:
                return 0
            if n>=1 and n<3:
                return 1
            memo[n]=tri(n-1,memo)+tri(n-2,memo)+tri(n-3,memo)
            return memo[n]
        return tri(n,{})
        