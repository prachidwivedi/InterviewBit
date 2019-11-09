# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        if(new_interval.start > new_interval.end):
            temp = new_interval.start
            new_interval.start = new_interval.end
            new_interval.end = temp
        intervals.append(new_interval)
        intervals.sort(key = lambda x : x.start)
        res = []
        for i in intervals:
            if res and res[-1].end >= i.start:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res
