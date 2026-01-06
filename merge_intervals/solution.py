class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        I'm given a list of intervals that are un-sorted and possibly overlapping. I need to merge all overlapping intervals
        and return an array such that all returned intervals are non-overlapping and cover all original intervals.

        I can first start by sorting the array by the start time of each interval. This helps to reduce the problem to the insert
        new interval problem. Then, I iterate through the array, comparing intervals to their immediate neighbor that comes after.
        I can detect if two intervals overlap if they don't satisfy the below conditions:
        - The end time of the current interval comes before the start time of the next interval
        - The start time of the current interval comes after the end time of the previous interval
        If the above two conditions are not true, the intervals should be merged.

        How should merging be handled? I can initialize a result array with the first entry in the input. Then, for subsequent
        intervals, I check if the last index of the result array overlaps with the current input interval. If it does not, I insert
        the current input interval into the result. If it does, I update the last entry in the result array with a merge interval
        of the current input interval and the last entry in the result array and continue iterating.

        time: O(nlog(n)) --> Initial sort time
        memory: O(n)
        """
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Initialize result
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # Check if the current input interval overlaps with the last entry of the result
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                # Update the last entry in res to be a merged interval
                res[-1] = [
                    min(res[-1][0], intervals[i][0]),
                    max(res[-1][1], intervals[i][1])
                ]
        return res
        
