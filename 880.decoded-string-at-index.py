#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#

# @lc code=start
class Solution:
    '''
    Key insight without crushing the memory
    The answer is always inside your input
    If a string is repeated n times, the kth character in the repeated string is the same as string[k % len(string)]
    For example "apple" repeated 6 times
    The 24th character is (24 % 5) = 4th in apple
    Therefore we can first go forward and then backward   
    
    '''

    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for c in s:
            if c.isalpha():
                size += 1
            else:
                size *= int(c)
        
        for c in reversed(s):
            k %= size
            if k == 0 and c.isalpha():
                return c
            if c.isalpha():
                size -= 1
            else:
                size //= int(c)
        
# @lc code=end

