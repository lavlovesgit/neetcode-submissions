
class Solution:
    memo={}
    def uniquePaths(self, m: int, n: int) -> int:
        if m==0 or n==0:
            return 0
        if m==1 and n==1:
            return 1
        key=(m,n)
        if key in self.memo:
            return self.memo[key]
        self.memo[key]=self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
        return self.memo[key]
        