#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    '''
    sliding window    
    '''
    def checkAppearances(self, count1, count2):
        count = 0
        for i in range(26):
            if count1[i] > count2[i]: return -1
            elif count1[i] == count2[i]: count += 1
        return abs(count - 26) > 0

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        else:
            seen1 = [0]*26
            seen2 = [0]*26
            for c in s1: seen1[ord(c) - ord('a')] += 1
            left = 0
            
            for right in range(len(s2)):
                seen2[ord(s2[right]) - ord('a')] += 1
                while self.checkAppearances(seen1, seen2) == 1:
                    seen2[ord(s2[left]) - ord('a')] -= 1
                    left += 1
                if self.checkAppearances(seen1, seen2) == 0: return True
            return False
# @lc code=end

