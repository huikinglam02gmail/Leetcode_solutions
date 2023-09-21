#
# @lc app=leetcode id=1904 lang=python3
#
# [1904] The Number of Full Rounds You Have Played
#

# @lc code=start
class Solution:
    '''
    Convert the times to mins
    if logout < login, + 24 * 60 to it
    Then // 15
    '''
    def ceilDiv(self, a, b):
        return -(a // -b)
    
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        login = int(loginTime[:2]) * 60 + int(loginTime[3:])
        logout = int(logoutTime[:2]) * 60 + int(logoutTime[3:])
        if login > logout:
            logout += 24 * 60
        return max(0, logout // 15 - self.ceilDiv(login, 15))
# @lc code=end

