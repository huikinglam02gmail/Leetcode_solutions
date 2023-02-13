#
# @lc app=leetcode id=1648 lang=python3
#
# [1648] Sell Diminishing-Valued Colored Balls
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    # Firstly, count and then sort the dictionary by keys in reverse order
    # For example if we have [10, 8, 6, 4, 2]
    # We denote width = available columns with same value inventory[i]
    # At each value we can sell = min(orders, (items[i] - items[i+1])* width)
    # We then take the division between sell and width: [quotient, remainder] = [sell // width, sell % width]
    # What we can earn from quotient is 
    # width*(item*(item + 1) // 2 - (item - quotient)*(item + 1 - quotient) // 2)
    # What we can earn from remainder is 
    # (item - quotient)*remainder
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = pow(10, 9) + 7
        counter = Counter(inventory)
        counterItems = list(counter.items())
        counterItems.append((0,0))
        counterItems.sort(key = lambda x: -x[0])
        
        result, width, ind = 0, 0, 0
        while orders > 0:
            width += counterItems[ind][1]
            sell = min(orders, (counterItems[ind][0] - counterItems[ind + 1][0])*width)
            q, r = divmod(sell, width)
            result += width * (counterItems[ind][0] * (counterItems[ind][0] + 1) - (counterItems[ind][0] - q) * (counterItems[ind][0] - q + 1)) // 2
            result += (counterItems[ind][0] - q) * r
            result %= MOD
            orders -= width * q
            orders -= r
            ind += 1
        return result



# @lc code=end

