#
# @lc app=leetcode id=2231 lang=python3
#
# [2231] Largest Number After Digit Swaps by Parity
#

# @lc code=start
class Solution:
    '''
    sort the odd and even digit and place in the respective indices
    '''
    def largestInteger(self, num: int) -> int:
        parity = [[], []]
        parityDigits = [[], []]
        for i, c in enumerate(str(num)):
            parity[int(c) % 2].append(i)
            parityDigits[int(c) % 2].append(int(c))
        final = [""] * len(str(num))
        for i in range(2): parityDigits[i].sort(reverse=True)
        for j in range(2):
            for i, d in zip(parity[j], parityDigits[j]): final[i] = str(d)
        return int("".join(final))

# @lc code=end

