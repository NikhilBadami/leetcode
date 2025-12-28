class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        One approach to this problem is to allocate an array the same size as nums and work backwards from the last index.
        Each index will store a boolean value indicating if the last index can be reached from that index. The final index
        is True by default. As I iterate backwards, I can check up to nums[i] spaces ahead to see if I can find a spot
        in the boolean array that can reach the final index. If I can, then I mark this space as True or False if I cannot.

        time: O(n^2)
        memory: O(n)
        """
        can_reach = [False] * len(nums)
        can_reach[-1] = True

        for i in range(len(nums)-2, -1, -1):
            if nums[i] != 0:
                # Iterate nums[i] times to see if a spot in the can_reach array is marked as True. If so, then this is a
                # reachable spot from which we can reach the end of the array
                for j in range(nums[i]+1):
                    if i+j < len(nums):
                        if can_reach[i+j] == True:
                            can_reach[i] = True
                            break
        return can_reach[0]

