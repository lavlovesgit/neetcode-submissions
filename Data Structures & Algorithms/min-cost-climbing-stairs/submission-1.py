class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={0:0,1:0}
        def minCost(i):
            if i in memo:
                return memo[i]
            memo[i]=min(cost[i-1]+minCost(i-1),cost[i-2]+minCost(i-2))
            return memo[i]
        return minCost(len(cost))
        