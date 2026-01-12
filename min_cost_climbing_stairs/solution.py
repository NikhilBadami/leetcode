class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        I'm given an array cost, which represents the cost of using a particular stair in a stair case. I need to find the minimum cost to reach
        the end of the staircase, which is the index after the end of the array. I can start on either the 0th index or the first and from each
        step I can take 1 or two steps.

        I can solve this by working backwards. I can create an array of len(cost)+1. The final index in this new array will represent the cost of
        getting to the top of the staircase from the top of the staircase, which is obviously 0. The second to last space is also a base case and
        is cost[-1]. After that, each cell is calculated as min(arr[i+1], arr[i+2]) + cost[i]. The return value is min(cost[0], cost[1])

        time: O(n)
        memory: O(n)
        """
        arr = [0] * (len(cost) + 1)
        arr[-2] = cost[-1]
        for i in range(len(cost) - 2, -1, -1):
            arr[i] = min(arr[i+1], arr[i+2]) + cost[i]
        return min(arr[0], arr[1])
        
