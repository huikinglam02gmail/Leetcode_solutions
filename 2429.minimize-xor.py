#
# @lc app=leetcode id=2429 lang=python3
#
# [2429] Minimize XOR
#

# @lc code=start
class Solution:
    '''
    Greedy
    First get number of set bits in num2
    Then for all 1s appearing in num1, put a 1 in corresponding position in x
    Then fill the remaining 1s from the right    
    '''
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_bit, num2_bit = bin(num1)[2:].zfill(31), bin(num2)[2:].zfill(31)
        available_one = num2_bit.count('1')
        x = ['0'] * 31
        for i in range(31):
            if num1_bit[i] == '1' and available_one > 0:
                x[i] = '1'
                available_one -= 1
        i = 30
        for i in range(30, -1, -1):
            if x[i] == '0' and available_one > 0:
                x[i] = '1'
                available_one -= 1
            i -= 1
        return int("".join(x),2)
        
        
        
        
# @lc code=end

