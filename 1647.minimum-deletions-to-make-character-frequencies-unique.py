#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
class Solution:
    '''
    build the hash table of character appearance frequency
    Then sort the keys by appearance value from low to high
    For example, "ceabaacb" -> "eccbbaaa"
    "e": 1; "c": 2; "b": 2; "a": 3
    take in e, c, and reject 2bs, take in a
    A greedy approach to fill in the 1,2,3,4... hash values increasingly    
    '''
    def minDeletions(self, s: str) -> int:
        hash_table = [0]*26
        for c in s:
            hash_table[ord(c)-ord('a')] += 1
        hash_table.sort(reverse = True)
        result = 0
        max_freq = hash_table[0]
        for count in hash_table:
            if count >= max_freq:
                result += count - max_freq
            else:
                max_freq = count
            if max_freq > 0:
                max_freq -= 1
        return result
# @lc code=end

