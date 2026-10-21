class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(x,n,memo):
            if x in memo:
                return memo[x]
            if (x==n):
                return 1
            if (x>n):
                return 0
            memo[x]=rec(x+1,n,memo)+rec(x+2,n,memo)
            return memo[x]
        return rec(0,n,{})
        
        