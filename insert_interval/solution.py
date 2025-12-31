class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        I'm given a set of intervals that do not overlap and are sorted in ascending order by start time. I need to insert a new
        interval into this list such that the non-overlapping and sorted nature is maintained. I can merge intervals if necessary
        to help maintain this property. There are many cases where a new interval could overlap with an existing one, for example,
        the new interval could start in an existing interval but end after, it could end in an existing interval and start before,
        it could be completely subsumed by an existing interval or vice versa. Trying to explicitly code all of these conditions
        could get hairy, so instead, it may be better to consider the conditions where the new interval does not overlap with an
        existing interval. While iterating through the intervals list, for any given interval I can check the following conditions:

        1: If the end time of the new interval occurrs before the start of the current interval, insert the new interval first
           followed by the existing interval. Because the input array is sorted, the first interval that satisfies this condition
           is guaranteed to be mark the insertion point
        2: If the end of the existing interval comes before the start of the new interval, insert the existing interval
        3: If the above conditions are not met, the intervals overlap and should be merged

        time: O(n)
        memory: O(1)
        """
        # Check edge case
        if len(intervals) == 0:
            return [newInterval]
        
        res = []
        inserted = False
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                if not inserted:
                    res.append(newInterval)
                res.append(intervals[i])
                inserted = True
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                # Intervals overlap and should be merged. Do not merge as the new merged interval could overlap with other intervals
                merge_start = min(newInterval[0], intervals[i][0])
                merge_end = max(newInterval[1], intervals[i][1])
                newInterval = [merge_start, merge_end]
        if not inserted:
            res.append(newInterval)
        return res
        
