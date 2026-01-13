class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        I am given an array of intervals and need to determine the minimum number of intervals I can remove to make the intervals non-overlapping.
        Determining if two intervals overlap is straight forward. For a given interval i, I can check if two intervals overlap by checking if the
        end time of the current interval is less than or equal to the start time of the next interval. If so, they do not overlap. If not, they
        do overlap (assume this check already passed for previous intervals starting at i=0).

        Keep in mind, I do not need to remove any intervals or modify the input, I simply need to determine the number of intervals I would have
        to remove. One thing I can do is split the intervals into two separate arrays, start and end. I can then sort each of these arrays and
        iterate through them seperately. I can think of the intervals as being set down along a number line. I start at time == 1, and as I
        iterate, I check to see how many intervals are started before the next timestamp in the end interval. The number of intervals to remove
        is the max number of overlapping intervals at any given time - 1 (since I need to keep one of the intervals).

        time: O(nlog(n)) --> Initial sort time
        memory: O(n)
        """
        # Pre-process intervals and sort arrays
        start = [i[0] for i in intervals]
        end = [i[1] for i in intervals]
        start.sort()
        end.sort()

        # Iterate through both arrays. Count the number of total overlapping arrays at any given time. This valus minus 1 is the number of
        # intervals to remove
        min_remove = 0
        num_overlapping = 0
        s = 0
        e = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                num_overlapping += 1
                min_remove = max(min_remove, num_overlapping - 1)
            else:
                # Technically we process ends first since [1,2] and [2,3] are technically not overlapping
                e += 1
                num_overlapping -= 1
        return min_remove

