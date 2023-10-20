#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

from typing import List


class NestedIterator:
    '''
    nested List is nothing special, the next function can be easily implemented by the keeping a stack
    '''
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]

    def next(self) -> int:
        result = self.stack[-1][0][self.stack[-1][1]].getInteger()
        self.stack[-1][1] += 1
        return result

    def hasNext(self) -> bool:
        while self.stack:
            nl, ind = self.stack[-1]
            if ind == len(nl):
                self.stack.pop()
            elif nl[ind].isInteger():
                return True
            else:
                self.stack[-1][1] += 1
                self.stack.append([nl[ind].getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

