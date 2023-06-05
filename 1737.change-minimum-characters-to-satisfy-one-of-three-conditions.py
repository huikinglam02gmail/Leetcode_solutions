#
# @lc app=leetcode id=1737 lang=python3
#
# [1737] Change Minimum Characters to Satisfy One of Three Conditions
#

# @lc code=start
class Solution:
    '''
    Since we can only convert to lower case letters, we can just brute force
    Scan letter c from 'a' to 'z', calculate the cost to change a and b such that the maximum / minimum of a / b is c
    Also, calculate the cost to turn all letters of a and b to c.
    Then for each condition, find out the minimum cost
    '''
    def minCharacters(self, a: str, b: str) -> int:
        aCount = [0]*26
        bCount = [0]*26
        for c in a:
            aCount[ord(c)-ord('a')] += 1
        for c in b:
            bCount[ord(c)-ord('a')] += 1

        aPrefix = [0]
        bPrefix = [0]
        for i in range(26):
            aPrefix.append(aPrefix[-1] + aCount[i])
            bPrefix.append(bPrefix[-1] + bCount[i])

        aAllBelow = [0]*26
        bAllBelow = [0]*26
        aAllBelow[0] = aPrefix[-1] - aPrefix[1]
        bAllBelow[0] = bPrefix[-1] - bPrefix[1]
        for i in range(1, 26):
            aAllBelow[i] = aAllBelow[i - 1] - aCount[i]
            bAllBelow[i] = bAllBelow[i - 1] - bCount[i]

        aAllAbove = [0]*26
        bAllAbove = [0]*26
        aAllAbove[-1] = aPrefix[-2]
        bAllAbove[-1] = bPrefix[-2]
        for i in range(24, -1, -1):
            aAllAbove[i] = aAllAbove[i + 1] - aCount[i]
            bAllAbove[i] = bAllAbove[i + 1] - bCount[i]
        
        aAllThis = [0]*26
        bAllThis = [0]*26
        for i in range(26):
            aAllThis[i] = aPrefix[-1] - aPrefix[i + 1] + aPrefix[i]
            bAllThis[i] = bPrefix[-1] - bPrefix[i + 1] + bPrefix[i]
        
        result = float('inf')
        for i in range(25):
            result = min(result, aAllBelow[i] + bAllAbove[i + 1])
        for i in range(25):
            result = min(result, bAllBelow[i] + aAllAbove[i + 1])
        for i in range(26):
            for j in range(26):
                result = min(result, aAllThis[i] + bAllThis[j])            
        return result
# @lc code=end
