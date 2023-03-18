#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

# @lc code=start
class ListNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = None
        self.prev = None
        
class BrowserHistory:
    '''
    Use a doubly linked list to achieve the purpose. During initiation, start with a List Node with name homepage. Then if we visit a new page, we make a new List Node and go forward. back and forward are moving back and front steps time   
    '''

    def __init__(self, homepage: str):
        self.cursor = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.cursor.next = ListNode(url)
        self.cursor.next.prev = self.cursor
        self.cursor = self.cursor.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.cursor.prev:
            self.cursor = self.cursor.prev
            steps -= 1
        return self.cursor.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cursor.next:
            self.cursor = self.cursor.next
            steps -= 1
        return self.cursor.val       


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end

