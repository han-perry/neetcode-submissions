class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    
        cost = cost[:]
        n = len(cost) - 1
        # cost[n-1] = cost[n]
        for i in range(n-2, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])