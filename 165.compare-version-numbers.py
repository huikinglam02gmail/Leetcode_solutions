#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def trimLeadingZero(self, versionSplit):
        vArr = []
        for part in versionSplit:
            p = 0
            while p < len(part) and part[p] == '0': p += 1
            if p == len(part): vArr.append('0')
            else: vArr.append(part[p:])
        return vArr
    

    def compareVersion(self, version1: str, version2: str) -> int:
        version1_split = version1.split('.')
        version2_split = version2.split('.')
        vArr1 = self.trimLeadingZero(version1_split)
        vArr2 = self.trimLeadingZero(version2_split)
        while len(vArr1) < len(vArr2): vArr1.append('0')
        while len(vArr2) < len(vArr1): vArr2.append('0')
        print(vArr1, vArr2)            
        for i in range(len(vArr2)):
            if len(vArr1[i]) > len(vArr2[i]): return 1
            elif len(vArr1[i]) < len(vArr1[i]): return -1
            elif vArr1[i] > vArr2[i]: return 1
            elif vArr1[i] < vArr2[i]: return -1
        return 0
# @lc code=end

