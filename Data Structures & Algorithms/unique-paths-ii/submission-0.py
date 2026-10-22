
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        def uniquePaths(m, n):
            if m == 0 or n == 0:
                return 0

            if obstacleGrid[m-1][n-1] == 1:
                return 0

            if m == 1 and n == 1:
                return 1

            key = (m, n)
            if key in memo:
                return memo[key]

            memo[key] = (
                uniquePaths(m-1, n) +
                uniquePaths(m, n-1)
            )

            return memo[key]

        return uniquePaths(m, n)
