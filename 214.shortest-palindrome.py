#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    '''
    We know the longest palindrome to form: s[::-1] + s
    We want to shrink down s[::-1] as much as possible while remaining palindrome.
    This is essentially asking the question to set up the lps array given a pattern:
    lps[i] = longest proper prefix in pattern[:i + 1] which is also a proper suffix in pattern[:i + 1]
    Here we use the pattern: s + "#" + s[::-1]
    After going through the whole pattern, we know s[-lps[-1]:] forms a palindrome by itself. We only need to add pattern[len(s) + 1:-lps[-1]]
    '''
    def shortestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        else:
            test_string = s + '#' + s[::-1]
            kmp = [0 for i in range(len(test_string))]
            for i in range(1, len(test_string), 1):
                kmp[i] = kmp[i - 1]
                while kmp[i] > 0 and test_string[i] != test_string[kmp[i]]: kmp[i] = kmp[kmp[i] - 1]
                if test_string[i] == test_string[kmp[i]]: kmp[i] += 1
            return test_string[len(s)+1:-kmp[-1]] + s
# @lc code=end

