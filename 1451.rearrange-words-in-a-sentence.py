#
# @lc app=leetcode id=1451 lang=python3
#
# [1451] Rearrange Words in a Sentence
#

# @lc code=start
class Solution:
    # Split the words by space
    # Then sort them by length, followed by ordering
    def arrangeWords(self, text: str) -> str:
        text_split = text.split(' ')
        text_split.sort(key = lambda x: len(x))
        for i in range(len(text_split)):
            if i == 0:
                text_split[i] = text_split[i][0].upper() + text_split[i][1:]
            else:
                text_split[i] = text_split[i][0].lower() + text_split[i][1:]
        return " ".join(text_split)
# @lc code=end

