#
# @lc app=leetcode id=1404 lang=python3
#
# [1404] Number of Steps to Reduce a Number in Binary Representation to One
#

# @lc code=start
class Solution:
    '''
    This does not ask for optimal number of steps
    So just simulate
    s[-1] will tell you whether it is zero or odd
    The simulation can be done by a real list, but it would involve rebuilding the list and modifying the list (n^2 time)
    But instead we could think about using pointer and number denoting carry over
    An extreme case is like this "1111"
    in the last digit we have 1, so we add 1, which will lead to 10000
    Then we divide by 2 by shifting to the right: 2 steps, 1000
    Therefore in the case we need to lengthen the list it will only occur once
    We can also denote the string as 111 + carry 1
    So now we do not need to add 1, just right shift: 1
    We stop when we are at index 0
    Basically the base line is we will shift at least n-1 times.
    Extra operation will be whether each digit is odd ofter operations    
    '''
    def numSteps(self, s: str) -> int:
        carry, result, n = 0, 0, len(s)
        result += n - 1
        for i in range(n - 1, 0, -1):
            if (int(s[i]) + carry) % 2 == 1:
                carry = 1
                result += 1
        return result + carry
    
    # @lc code=end

