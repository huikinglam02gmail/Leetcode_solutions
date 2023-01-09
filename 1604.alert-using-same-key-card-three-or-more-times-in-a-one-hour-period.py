#
# @lc app=leetcode id=1604 lang=python3
#
# [1604] Alert Using Same Key-Card Three or More Times in a One Hour Period
#

# @lc code=start
from typing import List


class Solution:
    # Convert time to minutes
    # Separate according to name
    # For each value in dict, binary search for number of entries within one hour
    
    def triedThrice(self, name):
        for i, t in enumerate(self.hashTable[name]):
            if i > 1 and self.hashTable[name][i] - self.hashTable[name][i - 2] <= 60:
                return True
        return False
    
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        self.hashTable = {}
        for name, time in zip(keyName, keyTime):
            if name not in self.hashTable:
                self.hashTable[name] = []
            self.hashTable[name].append(60*int(time[0:2]) + int(time[3:5]))
        
        result = []
        for key in sorted(list(self.hashTable.keys())):
            self.hashTable[key].sort()
            if self.triedThrice(key):
                result.append(key)        
        return result

        
# @lc code=end

