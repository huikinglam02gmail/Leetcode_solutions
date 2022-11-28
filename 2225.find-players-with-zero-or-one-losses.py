#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#

# @lc code=start
class Solution:
    # for each match, record winner and loser in a hashTable
    # key = player; value = [# won, # lost]
    # return [keys with # lost = 0, keys = # lost = 1]
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hashTable = {}
        for w, l in matches:
            if w not in hashTable:
                hashTable[w] = [0, 0]
            if l not in hashTable:
                hashTable[l] = [0, 0]
            hashTable[w][0] += 1
            hashTable[l][1] += 1
        result = [[], []]
        for key in sorted(hashTable.keys()):
            if hashTable[key][1] == 0:
                result[0].append(key)
            elif hashTable[key][1] == 1:
                result[1].append(key)
        return result
# @lc code=end

