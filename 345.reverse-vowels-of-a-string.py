#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        string_list = []
        for c in s:
            string_list.append(c)
        vowels = "aeiouAEIOU"
        left, right = 0, len(string_list)-1
        while left < right:
            if string_list[left] not in vowels:
                left += 1
            elif string_list[right] not in vowels:
                right -= 1
            else:
                string_list[left], string_list[right] = string_list[right], string_list[left]
                left += 1
                right -= 1
        return "".join(string_list)
        
# @lc code=end

