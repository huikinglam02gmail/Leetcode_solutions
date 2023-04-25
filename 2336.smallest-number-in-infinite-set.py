#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
class SmallestInfiniteSet:

    def __init__(self):
        self.lost = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        item = self.smallest
        self.lost.add(item)
        while self.smallest in self.lost:
            self.smallest += 1
        return item

    def addBack(self, num: int) -> None:
        if num in self.lost:
            self.lost.remove(num)
        if num < self.smallest:
            self.smallest = num


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

