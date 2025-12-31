"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        I'm given a list of intervals that contains meeting start and end times and need to
        determine how many days it would take to be able to schedule all of the meetings. Any
        overlapping meetings cannot be scheduled on the same day, so this problem becomes finding
        a way to determine how many meetings are overlapping with each other at any given time,
        and the maximum number of overlapping meetings is the number of days needed to schedule
        all meetings.

        This can be done by splitting the start and end times for each interval into separate
        arrays, and then sorting them. Once this is done, I can iterate through both arrays using
        two pointers. The start array tells me how many meetings have been started. A meeting
        ends when an end time is greater than or equal to the current start time, in other words,
        I am assuming some kind of timestamp that is being tracked. For example, in the arrays
        below, a meeting starts at time 0. I don't need to explicitly loop through the timestamps.
        At time 5, I can see that another meeting starts, but the earliest end time is still
        in the future, so these meetings must overlap. At the next time stamp, I see that a
        meeting starts at timestamp 15, but a meeting ends at timestamp 10, therefore a meeting has
        ended, and I decrement my days counter. Once I have exhausted my start time list, there
        are no more meetings that can be started. I return the max value for days encountered
        while scanning these lists.

        [0, 5, 15]
        [10, 20, 40]

        time: O(nlog(n) + n) --> Need to create start/end time arrays and sort
        memory: O(n)
        """
        # Check edge case
        if len(intervals) == 0:
            return 0
        
        # Create start and end time arrays
        start_times = [i.start for i in intervals]
        start_times.sort()
        end_times = [i.end for i in intervals]
        end_times.sort()

        # Scan through arrays to detect overlapping meetings
        max_days = 0
        days = 0
        s = 0
        e = 0
        while s < len(intervals):
            if end_times[e] <= start_times[s]:
                days -= 1
                e += 1
            else:
                days += 1
                s += 1
                max_days = max(days, max_days)
        return max_days

