#
# @lc app=leetcode id=1702 lang=python3
#
# [1702] Maximum Binary String After Change
#

# @lc code=start
class Solution:
    '''
    For all leading ones in binary, do not touch them (p)
    From the first 0, do operation 2 to push all 1s to the end of binary. As operation 2 conserves number of 1 and 0, we will get k 1s at the end of string. (assuming there are j 0s and (n - p - j) 1s after the p 1s, the final string would be p*1 + j*0 + (n - p - j)*1)
    Then we operate on the j 0s until it reaches the boundary. The final 0 will be the last 0 i.e. at p + j - 1
    Edge case: if there are no "0", just return binary
    '''
    def maximumBinaryString(self, binary: str) -> str:
        i, j, p, n = 0, 0, 0, len(binary)
        while i < n and binary[i] == "1":
            p += 1
            i += 1
        while i < n:
            if binary[i] == "0":
                j += 1
            i += 1
        return binary if n == p else (p + j - 1)*"1" + "0" + (n - p - j)*"1"
# @lc code=end

