#
# @lc app=leetcode id=2933 lang=python3
#
# [2933] High-Access Employees
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    '''
    Convert access time to minutes, keep track of the access times within the last hour in a deque
    '''
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        result = set()
        data = [[name, 60 * int(time[:2]) + int(time[2:])] for name, time in access_times]
        data.sort(key=lambda x: x[1])
        hashTable = {}
        for name, time in data:
            if name not in hashTable: hashTable[name] = deque()
            while hashTable[name] and time - hashTable[name][0] >= 60: hashTable[name].popleft()
            if len(hashTable[name]) >= 2: result.add(name)
            hashTable[name].append(time)
        return list(result)
# @lc code=end

