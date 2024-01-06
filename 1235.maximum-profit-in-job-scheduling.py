#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start
import bisect
from operator import itemgetter
from typing import List


class Solution:
    '''
    Well, since profit can vary independently of start time and end time, we should think about DP approach (structured brute-force)
    Firstly, group [startTime, endTime, profit] together: jobs
    Then sort according to startTime
    dp[jobs[i]] = max profit possible given jobs[i:]
    we want max(dp[:])    
    '''

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for s, e, p in zip(startTime, endTime, profit):
            jobs.append([s, e, p])
        jobs.sort(key = lambda x: x[0])
        n = len(jobs)
        result = [0] * n
        for i in range(n - 1, -1, -1):
            currentProfit = jobs[i][2]
            index = bisect.bisect_left(jobs, jobs[i][1], key = itemgetter(0))
            if index < n: currentProfit += result[index]
            if i < n - 1: result[i] = result[i + 1]
            result[i] = max(result[i], currentProfit)
        return result[0]
# @lc code=end

