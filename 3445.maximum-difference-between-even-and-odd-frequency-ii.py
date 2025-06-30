#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution:
    '''
    s consists only of digits '0' to '4'.
    We can probe through a and b pairs
    For s[i:j], we are asked to maximize (count['a'][:j] - count['b'][:j]) - (count['a'][:i] - count['b'][:i]),
    which is equivalent to finding the minimum of (count['a'][:i] - count['b'][:i]), subjected to:
    1. j - i >= k
    2. count['b'][:j] - count['b'][:i] >= 2
    3. given we known count['a'][:j] - count['b'][:j], with state = count['a'][:j] % 2 * 2 + count['b'][:j] % 2,
    We can get s[i:j] satisfying the odd / even conditions by looking up the minimum of state ^ 2
    '''

    def getStatus(self, aCount, bCount):
        return (aCount % 2) * 2 + (bCount % 2)

    def maxDifference(self, s: str, k: int) -> int:
        allCharacters = '01234'
        result = - float("inf")
        for a in allCharacters:
            for b in allCharacters:
                if a == b: continue
                left = -1
                best = [float("inf")] * 4
                aCount = 0
                bCount = 0
                prevCounta = 0
                prevCountb = 0
                
                for right in range(len(s)):
                    if s[right] == a: aCount += 1
                    elif s[right] == b: bCount += 1
                    
                    while right - left >= k and bCount - prevCountb >= 2:
                        best[self.getStatus(prevCounta, prevCountb)] = min(best[self.getStatus(prevCounta, prevCountb)], prevCounta - prevCountb)
                        left += 1
                        if s[left] == a: prevCounta += 1
                        elif s[left] == b: prevCountb += 1
                    
                    if best[self.getStatus(aCount, bCount) ^ 2] != float("inf"): result = max(result, (aCount - bCount) - best[self.getStatus(aCount, bCount) ^ 2])
        return result
# @lc code=end

