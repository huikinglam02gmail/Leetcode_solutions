#
# @lc app=leetcode id=2075 lang=python3
#
# [2075] Decode the Slanted Ciphertext
#

# @lc code=start
class Solution:
    '''
    col = len(encodedText) // row
    '''
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        result = []
        cols = len(encodedText) // rows
        for i in range(cols):
            cur = i
            while cur < len(encodedText):
                result.append(encodedText[cur])
                cur += cols + 1
        while result and result[-1] == " ": result.pop()
        return "".join(result)
        
# @lc code=end

