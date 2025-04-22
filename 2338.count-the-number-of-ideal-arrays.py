#
# @lc app=leetcode id=2338 lang=python3
#
# [2338] Count the Number of Ideal Arrays
#

# @lc code=start
import math


class Solution:
    '''
    Count all the possibilities by combinatorics
    Firstly, we notice that [1,1,...,1] to [maxValue, maxValue,...] are always ideal
    Next, we try to construct ideal arrays that involves more than one type of values
    To do that, we record all the beginning values 1: max_Value
    For 1, all the values are eligible. We first start with only one other value, from 2 to maxValue
    Let's start with 2. In an array of n = 5, first value is fixed, [1,?,?,?,?], we are free to put in 1 & 2s in the positions, as long as all 1s are put before 2, and 2 must appear
    I prefer thinking about this a little differently, where is the transition point between 1 and 2?
    it could be at position 1: [1,2,2,2,2], 2: [1,1,2,2,2], 3: [1,1,1,2,2], 4: [1,1,1,1,2] but no more. We cannot have [1,1,1,1,1].
    In short, we are choosing 1 transition point from (n - 1) possibilities
    Therefore (n-1) C k ways
    So the procedure is rather simple: we progressively increment the number of elements to put into the array and keep counting the number of ways
    The hash table is for counting how many ways the last biggest number in the array can be reached. For example, numbers like 32 can be 2*16 and  4*8
    '''
    def idealArrays(self, n: int, maxValue: int) -> int:
        result, MOD = maxValue, pow(10, 9) + 7
        table = {}
        for i in range(1, maxValue + 1): table[i] = 1
        for k in range(1, n):
            temp = {}
            for last_int in table:
                for j in range(2, maxValue // last_int + 1):
                    result += math.comb(n - 1, k) * table[last_int]
                    result %= MOD
                    temp[j * last_int] = temp.get(j * last_int, 0) + table[last_int]
            table = temp
        return result
# @lc code=end

