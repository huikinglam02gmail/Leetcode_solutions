#
# @lc app=leetcode id=1813 lang=python3
#
# [1813] Sentence Similarity III
#

# @lc code=start
class Solution:
    '''
    Split the sentences by space
    We can only insert words into the shorter sentence sShort and try to become the longer sentence sLong
    Use a two-pointer approach: if we see in current word in sShort is different from that in sLong, we increment numSkip by 1
    whenever we see numSkip = 2, we return false  
    return true when reached sentence end
    We need to try in both directions
    '''
    def similar(self, s1Split, s2Split):
        i, j, numSkip = 0, 0, 0
        while i < len(s1Split) and j < len(s2Split):
            if s2Split[j] != s1Split[i]:
                numSkip += 1
                if numSkip > 1: return False
                while i < len(s1Split) and s1Split[i] != s2Split[j]:
                    i += 1
            else:
                i += 1
                j += 1
        return (j == len(s2Split) and i == len(s1Split) and numSkip <= 1) or (i < len(s1Split) and numSkip == 0)

    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1Split, s2Split = sentence1.split(" "), sentence2.split(" ")
        if len(s1Split) < len(s2Split):
            s1Split, s2Split = s2Split, s1Split
        return self.similar(s1Split, s2Split) or self.similar(s1Split[::-1], s2Split[::-1])
# @lc code=end

