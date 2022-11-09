#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:
    # Use a monotonic decreasing stack to achieve the goal
    def __init__(self):
        self.stack = [[100001, -1]]
        self.count = 0

    def next(self, price: int) -> int:
        if price < self.stack[-1][0]:
            ans = 1
        else:
            while price >= self.stack[-1][0]:
                self.stack.pop()
            ans = self.count - self.stack[-1][1]
        self.stack.append([price, self.count])
        self.count += 1
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

