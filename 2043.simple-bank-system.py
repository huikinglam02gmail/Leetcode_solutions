#
# @lc app=leetcode id=2043 lang=python3
#
# [2043] Simple Bank System
#

# @lc code=start
from typing import List


class Bank:
    '''
    just implement as described
    '''

    def __init__(self, balance: List[int]):
        self.Balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 - 1 < 0 or account1 - 1 > len(self.Balance): return False
        if account2 - 1 < 0 or account2 - 1 > len(self.Balance): return False
        if self.Balance[account1 - 1] < money: return False
        self.Balance[account1 - 1] -= money
        self.Balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account - 1 < 0 or account - 1 > len(self.Balance): return False
        self.Balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account - 1 < 0 or account - 1 > len(self.Balance): return False
        if self.Balance[account - 1] < money: return False
        self.Balance[account - 1] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
# @lc code=end

