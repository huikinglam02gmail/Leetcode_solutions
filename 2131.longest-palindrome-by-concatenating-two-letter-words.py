#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#

# @lc code=start
class Solution:
    # all words are of length 2, so only 2 possibilities
    # "XX", itself, can always be used even times. Only one odd extra might be inserted in the middle
    # "XY" and "YX" pairs: minimum of them
    def longestPalindrome(self, words: List[str]) -> int:
        hash_table = {}
        for word in words:
            if word not in hash_table:
                hash_table[word] = 0
            hash_table[word] += 1
        keys = list(hash_table.keys())
        result, considered, same_odd_set = 0, set(), set()
        for key in keys:
            if key not in considered:
                considered.add(key)
                if key[0] == key[1]:
                    result += 4* (hash_table[key] // 2)
                    if hash_table[key] % 2 == 1:
                        same_odd_set.add(key)
                elif key[1] + key[0] in hash_table:
                    result += 4*min(hash_table[key], hash_table[key[1]+key[0]])
                    if key[1]+key[0] not in considered:
                        considered.add(key[1]+key[0]) 

        if len(same_odd_set) > 0:
            result += 2
        return result
# @lc code=end

