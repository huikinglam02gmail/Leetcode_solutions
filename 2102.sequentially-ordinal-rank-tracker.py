#
# @lc app=leetcode id=2102 lang=python3
#
# [2102] Sequentially Ordinal Rank Tracker
#

# @lc code=start
class SORTracker:

    def __init__(self):
        self.sl = SortedList()
        self.count = 0

    def add(self, name: str, score: int) -> None:
        self.sl.add([- score, name])

    def get(self) -> str:
        self.count += 1
        return self.sl[self.count - 1][1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
# @lc code=end

