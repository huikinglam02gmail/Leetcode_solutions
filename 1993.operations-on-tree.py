#
# @lc app=leetcode id=1993 lang=python3
#
# [1993] Operations on Tree
#

# @lc code=start
from typing import List


class LockingTree:
    '''
    Design according to the instructions:
    lock, unlock: we want to store locked status as lock[i] = [true or false, user id or -1]
    upgrade:
    action: unlock all descendants -> we can build the graph of descendants and dfs from the node, if the following are satisfied:
    1. lock[num] == [false, -1]
    2. ancestor search by parent always is [false, -1]
    3. dfs from num and return true if one of the descendant is locked
    '''

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        self.status = [[False, -1] for i in range(n)]
        self.children = [set() for i in range(n)]
        for i, p in enumerate(self.parent):
            if p >= 0:
                self.children[p].add(i)

    def lock(self, num: int, user: int) -> bool:
        if self.status[num][0]:
            return False
        self.status[num] = [True, user]
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.status[num][0] and self.status[num][1] == user:
            self.status[num] = [False, -1]
            return True
        return False     

    def hasLockedAncestors(self, node):
        if node == -1:
            return False
        elif self.status[node][0]:
            return True
        else:
            return self.hasLockedAncestors(self.parent[node])
        
    def hasLockedDescendents(self, node):
        if self.status[node][0]:
            return True
        for child in self.children[node]:
            if self.hasLockedDescendents(child):
                return True
        return False
    
    def unLockDescendents(self, node):
        self.status[node] = [False, -1]
        for child in self.children[node]:
            self.unLockDescendents(child)

    def upgrade(self, num: int, user: int) -> bool:
        if self.hasLockedAncestors(num) or not self.hasLockedDescendents(num):
            return False
        self.unLockDescendents(num)
        self.lock(num, user)
        return True

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
# @lc code=end

