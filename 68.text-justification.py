#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
from typing import List


class Solution:
    '''
    Do this row by row
    Keep check of current rowlength
    Keep row words in list    
    '''
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        j = 0
        wordLengthAccumulated = 0
        result = []
        n = len(words)
        for i in range(n):
            if wordLengthAccumulated + i - j + len(words[i]) > maxWidth:
                row = words[j]
                remainingEmptySpace = maxWidth - wordLengthAccumulated
                wordLengthAccumulated -= len(words[j])
                j += 1
                if i == j:
                    row += remainingEmptySpace * " "
                else:
                    shortest = remainingEmptySpace // (i - j)
                    while j < i:
                        if (remainingEmptySpace % (i - j)) > 0:
                            row += (shortest + 1) * " "
                            remainingEmptySpace -= shortest + 1
                        else:
                            row += shortest * " "
                            remainingEmptySpace -= shortest
                        row += words[j]
                        wordLengthAccumulated -= len(words[j])
                        j += 1
                result.append(row)
            wordLengthAccumulated += len(words[i])
        row = ""
        while wordLengthAccumulated > 0:
            row += words[j]
            wordLengthAccumulated -= len(words[j])
            if wordLengthAccumulated > 0:
                row += " "
                j += 1
        while len(row) < maxWidth:
            row += " "
        result.append(row)
        return result

# @lc code=end

