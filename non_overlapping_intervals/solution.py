class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        I'm given an array of intervals and I need to determine the minimum number of intervals to remove such that all remaining intervals do not
        overlap. I can do this as follows: first, I sort the array by start time. Then, I iterate through the array and make a series of
        comparisons. I start with the first interval in the list and then compare it to subsequent intervals. For every interval the first
        interval overlaps with, I keep the interval that ends earlier. I can determine if two intervals overlap by checking if the start time
        of the subsequent interval comes after the end time of the current interval. If this condition is not true, the intervals overlap. If
        the intervals do not overlap, I update the current interval to the one with the later end time. I only need a single counter to track
        how many intervals I am removing. Every time two intervals overlap, I increment this counter.

        time: O(nlog(n)) --> sorting
        memory: O(1)
        """
        # Sort input by start time
        intervals.sort(key=lambda x: x[0])

        # Starting with the first interval in the list, iterate through and perform comparisons
        min_remove = 0
        cur_interval = intervals[0]
        for i in range(1, len(intervals)):
            # Check if current interval overlaps with intervals[i]
            if intervals[i][0] >= cur_interval[1]:
                # Intervals do not overlap. Update current interval
                cur_interval = intervals[i]
            else:
                # Intervals overlap. Keep the one with the earlier end time
                cur_interval = cur_interval if cur_interval[1] < intervals[i][1] else intervals[i]
                min_remove += 1
        return min_remove
        
