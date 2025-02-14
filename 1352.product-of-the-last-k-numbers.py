#
# @lc app=leetcode id=1352 lang=python3
#
# [1352] Product of the Last K Numbers
#

# @lc code=start
class ProductOfNumbers:
    '''
    Use a prefix product array to keep the cumulative product seen
    An edge case if num = 0, which if not taken care of will make all prefix product afterwards becomes 0
    We can reset the prefix array if that happens    
    '''
    def __init__(self):
        self.prefix = [1]
        
    def add(self, num: int) -> None:
        if num != 0: self.prefix.append(self.prefix[-1]*num)
        else: self.prefix = [1]

    def getProduct(self, k: int) -> int:
        if len(self.prefix) >= k + 1: return self.prefix[-1] // self.prefix[-k-1]
        else: return 0

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @lc code=end

