#
# @lc app=leetcode id=1825 lang=python3
#
# [1825] Finding MK Average
#

# @lc code=start
from collections import deque
import sortedcontainers
class MKAverage:
    '''
    Break down the task in hand:
    We want to keep m last numbers in check, have these numbers sorted, such that the top and bottom k elements can be accessed quickly. 
    But we also want to update the tree regularly. We cannot afford to calculate the largest and smallest k - sums every time a query is make, so we need to maintain the left and right sums. When a new number nums[i] comes in, we first find where is nums[i - m]. We identify if it is in the smallest and largest k sums, and if so, deduct it from  the sums. Also, we need to deduct it from the total sum.
    Then we insert nums[i]. We first ask where the insertion position should be, and update the two k sums and totalSum
    When calculateMKAverage is called, we just return (totalSum - leftkSum - rightkSum) // (m - 2 * k)
    '''
    def __init__(self, m: int, k: int):
        self.tree = sortedcontainers.SortedList()
        self.Total = 0
        self.leftSum = 0
        self.rightSum = 0
        self.index = -1
        self.m = m
        self.k = k
        self.dq = deque()

    def addElement(self, num: int) -> None:
        self.index += 1
        if len(self.dq) == self.m:
            value, index = self.dq.popleft()
            treeIndex = self.tree.index([value, index])
            if treeIndex < self.k:
                self.leftSum -= value
            if self.m - treeIndex <= self.k:
                self.rightSum -= value
            self.Total -= value
            self.tree.remove([value, index])
        newNode = [num, self.index]
        indLeft= self.tree.bisect_left(newNode)
        indRight = self.tree.bisect_right(newNode)
        print(num, indLeft, indRight)
        if len(self.dq) == self.m - 1 and indLeft < self.k:
            self.leftSum -= self.tree[indLeft][0]
            self.leftSum += num
        if len(self.dq) == self.m - 1 and self.m - indRight <= self.k:
            self.rightSum -= self.tree[indRight][0]
            self.rightSum += num
        self.Total += num
        self.tree.add(newNode)
        self.dq.append(newNode)

    def calculateMKAverage(self) -> int:
        return -1 if len(self.tree) < self.m else (self.Total - self.leftSum - self.rightSum) // (self.m - 2 * self.k)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
# @lc code=end

