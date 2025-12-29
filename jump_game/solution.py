class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        We need to see if we can reach the final index in the array starting from the beginning. One approach is to use
        dynamic programming to cache results starting from the end of the array to see if that position can reach the end.
        This solution is O(n^2) because it searches starting from the current index to see if any of the indices in a
        separate array, can_reach, is True, indicating that that spot can reach the end, meaning the current spot can also
        reach the end.

        We don't need to actually do this iteration, though. Instead, we can check if the current index + the current number
        can reach or exceed the end marker. The end marker in this case will replace the can_reach array. The end_marker
        represents the farthest back index we can reach from the current position. When we find a position that can reach
        the current end marker, we update the end marker to the current index. If the end marker eventually reaches index 0,
        we know we can reach the end.

        time: O(n)
        memory: O(1)
        """
        end_marker = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= end_marker:
                end_marker = i
        return True if end_marker == 0 else False
