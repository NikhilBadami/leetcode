class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        The goal of this problem is to insert a new interval into a list of intervals sorted by their start time. After
        insertion there should be no overlapping intervals, so interval should be merged if necessary.

        Merging intervals will fall under one of the three conditions below:

        1: If the end of the new interval comes before the start of an existing interval, insert the new interval first,
           then insert the existing interval. Assume the interval did not overlap with any previous intervals
        2: If the start of the new interval comes after the end of an existing one, insert the existing interval, but
           do not insert the new interval yet as it may overlap with future intervals
            - Have a check in case we make it to the end of iteration and the interval was not inserted
        3: If neither of the above conditions are true, the new interval overlaps with the existing interval. In this
           case create a new merge interval as follows:
                new_start = min(insert_start, existing_start)
                new_end = max(insert_end, existing_end)
            continue iteration and try to either insert or merge this new interval based on the above 3 conditions
        
        time: O(n)
        memory: O(n)
        """
        # Edge case
        if len(intervals) == 0:
            return [newInterval]
        
        res = []
        inserted = False
        for interval in intervals:
            if newInterval[1] < interval[0]:
                # Condition 1
                if not inserted:
                    res.append(newInterval)
                res.append(interval)
                inserted = True
            elif newInterval[0] > interval[1]:
                # Condition 2
                res.append(interval)
            else:
                # Condition 3
                new_start = min(newInterval[0], interval[0])
                new_end = max(newInterval[1], interval[1])
                newInterval = [new_start, new_end]
        if not inserted:
            res.append(newInterval)
        return res

