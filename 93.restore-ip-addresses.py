#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from typing import List


class Solution:
    def isok(self, arr):
        for i in range(4):
            if len(arr[i]) > 1 and arr[i][0] == "0":
                return False
            if int(arr[i]) > 255:
                return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        if len(s) >= 4:
            arr = []
            for i in range(1,len(s)-2):
                arr.append(s[:i])
                for j in range(i+1,len(s)-1,1):
                    arr.append(s[i:j])
                    for k in range(j+1,len(s),1):
                        arr.append(s[j:k])
                        arr.append(s[k:])
                        if self.isok(arr):
                            result.append('.'.join(arr))
                        arr.pop()
                        arr.pop()
                    arr.pop()
                arr.pop()
        return result
                            
        
# @lc code=end

