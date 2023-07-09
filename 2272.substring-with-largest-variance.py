#
# @lc app=leetcode id=2272 lang=python3
#
# [2272] Substring With Largest Variance
#

# @lc code=start
class Solution:
    '''
    The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string.
    So we need to consider any two pairs. Because we only need to consider 26 * 26 = 676 character pairs, and within each pair, all other characters are irrelevant. for pair ("a", "b"), we are assign "a" = +1 and "b" = -1, and all characters will not enter the List. This problem is then a maximum subarray sum problem, solvable by Kadane. There is a catch though: unlike in Kadane, we would like ensure all the subarrays of interest has both "a" and "b"
    '''

    def Kadane(self, arr):
        current, result, beginMinus, hasMinus = 0, 0, False, False
        for num in arr:
            if num == -1:
                hasMinus = True
                if current >= 0 and beginMinus:
                    beginMinus = False
                    current += 1           
            current += num
            if current < 0:
                current = -1
                beginMinus = True
            elif hasMinus:
                result = max(result, current)
        return result


    def largestVariance(self, s: str) -> int:
        result = 0
        occur = [[] for i in range(26)]

        for i, c in enumerate(s):
            occur[ord(c) - ord('a')].append(i)

        for i in range(25):
            for j in range(i + 1, 26):
                if len(occur[i]) > 0 and len(occur[j]) > 0:
                    subArray, pi, pj = [], 0, 0
                    # Two pointers merge
                    while pi < len(occur[i]) and pj < len(occur[j]):
                        if occur[i][pi] < occur[j][pj]:
                            subArray.append(1)
                            pi += 1
                        else:
                            subArray.append(-1)
                            pj += 1                            
                    while pi < len(occur[i]):
                        subArray.append(1)
                        pi += 1
                    while pj < len(occur[j]):
                        subArray.append(-1)
                        pj += 1
                    result = max(result, self.Kadane(subArray))
                    result = max(result, self.Kadane([- i for i in subArray]))
        return result
# @lc code=end

