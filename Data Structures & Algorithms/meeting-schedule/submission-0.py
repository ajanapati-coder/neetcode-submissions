class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedIntervals = sorted(intervals, key=lambda x: x.start)
        for i in range(len(sortedIntervals) - 1):
            if sortedIntervals[i + 1].start < sortedIntervals[i].end:
                return False

        return True