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
    But we also want to update the tree regularly. We cannot afford to calculate the largest and smallest k - sums every time a query is make, so we need to maintain the left and right sums. 
    When a new number nums[i] comes in, we first find where is nums[i - m]. This node we must remove. We identify if it is in the left and right k sums, and if so, deduct it from the sums. Note that we also need to add the kth smallest element and the m - k th smallest element. Also, we need to deduct it from the total sum.
    Then we insert nums[i]. We first ask where the insertion position should be, and update the two k sums and totalSum in similar manner as before

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
    
    def deleteNode(self, num, ind):
        treeIndex = self.tree.index([num, ind])
        if treeIndex < self.k:
            self.leftSum -= num
            self.leftSum += self.tree[self.k][0]
        if len(self.dq) + 1 - treeIndex <= self.k:
            self.rightSum -= num
            self.rightSum += self.tree[len(self.dq)- self.k][0]
        self.tree.remove([num, ind])
        self.Total -= num
    
    def insertNode(self, num, ind):
        self.tree.add([num, ind])
        treeIndex = self.tree.bisect_left([num, ind])
        if treeIndex < self.k:
            self.leftSum += num
            if len(self.dq) > self.k:
                self.leftSum -= self.tree[self.k][0]
        if len(self.dq) - treeIndex <= self.k:
            self.rightSum += num
            if len(self.dq) > self.k:
                self.rightSum -= self.tree[len(self.dq) - self.k - 1][0]
        self.Total += num
        
    def addElement(self, num: int) -> None:
        self.index += 1
        if len(self.dq) == self.m:
            value, index = self.dq.popleft()
            self.deleteNode(value, index)
        self.dq.append([num, self.index])
        self.insertNode(num, self.index)

    def calculateMKAverage(self) -> int:
        return -1 if len(self.tree) < self.m else (self.Total - self.leftSum - self.rightSum) // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

