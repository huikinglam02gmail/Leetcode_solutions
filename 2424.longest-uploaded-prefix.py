#
# @lc app=leetcode id=2424 lang=python3
#
# [2424] Longest Uploaded Prefix
#

# @lc code=start
class LUPrefix:

    def __init__(self, n: int):
        self.seen = [False] * n
        self.pref = 0
        self.n = n

    def upload(self, video: int) -> None:
        self.seen[video - 1] = True
        while self.pref < self.n and self.seen[self.pref]: self.pref += 1

    def longest(self) -> int:
        return self.pref


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
# @lc code=end

