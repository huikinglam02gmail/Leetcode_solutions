#
# @lc app=leetcode id=3306 lang=python3
#
# [3306] Count of Substrings Containing Every Vowel and K Consonants II
#

# @lc code=start
from collections import deque


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowelTable = {}
        result = 0
        l = 0
        dqConsonants = deque()
        for i, c in enumerate(word):
            if c in "aeiou": 
                if c not in vowelTable: vowelTable[c] = deque()
                vowelTable[c].append(i)
            else: dqConsonants.append(i)
            while len(dqConsonants) > k:
                if word[l] in "aeiou":
                    vowelTable[word[l]].popleft()
                    if not vowelTable[word[l]]: vowelTable.pop(word[l])
                else: dqConsonants.popleft() 
                l += 1
            if len(vowelTable) == 5 and len(dqConsonants) == k:
                firstEssentialIndex = min(vowelTable[c1][-1] for c1 in "aeiou")
                if dqConsonants: firstEssentialIndex = min(firstEssentialIndex, dqConsonants[0])
                result += firstEssentialIndex - l + 1
        return result
        
# @lc code=end

