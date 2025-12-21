#
# @lc app=leetcode id=3775 lang=python3
#
# [3775] Reverse Words With Same Vowel Count
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        sSplit = s.split(' ')
        countFirst = sSplit[0].count('a') + sSplit[0].count('e') + sSplit[0].count('i') + sSplit[0].count('o') + sSplit[0].count('u')
        resultSplit = []
        for i, split in enumerate(sSplit):
            vowelCount = 0
            for char in split:
                if char.lower() in 'aeiou':
                    vowelCount += 1
            if i > 0 and vowelCount == countFirst:
                resultSplit.append(split[::-1])
            else:
                resultSplit.append(split)
        return ' '.join(resultSplit)
            
# @lc code=end

