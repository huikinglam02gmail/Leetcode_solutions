#
# @lc app=leetcode id=2030 lang=python3
#
# [2030] Smallest K-Length Subsequence With Occurrences of a Letter
#

# @lc code=start
class Solution:
    '''
    This is a problem as a combination of 1673. Find the Most Competitive Subsequence and 316. Remove Duplicate Letters, in which both can be solved with a stack.
    We first count the number of occurrences of letter inside s.
    Then we consider each character from left to right. We first check if it is smaller than the stack top and if we pop from the stack, we have enough characters afterwards to fill the stack back to at least size k (same requirement as 1673). The additional requirement in here is we want to make sure the element we pop out is not letter or we have enough letter left behind to fill in at least repetition times afterwards
    Notice we only append the current character c if 廿he current stack is shorter than k. And:
    1. c == letter (it's always advantageous to put more "letter" in the stack) or
    2. if c != letter, if we add c to the stack, what's left to be filled k - len(stack) > repetition (so that we will not violate the requirement afterwards)
    repetition here means number of "letter" missing in stack to fulfil the requirement. So it can be negative in here
    '''
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        stack = []
        n = len(s)
        usableLetterBehind = s.count(letter)
        for i, c in enumerate(s):
            while stack and c < stack[-1] and n - i + len(stack) > k and (stack[-1] != letter or usableLetterBehind > repetition):
                if stack.pop() == letter: repetition += 1
            if c == letter: usableLetterBehind -= 1
            if len(stack) < k:
                if c == letter: 
                    stack.append(c)
                    repetition -= 1
                elif k - len(stack) > repetition:
                    stack.append(c)                
        return "".join(stack)
# @lc code=end

