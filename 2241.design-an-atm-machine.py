#
# @lc app=leetcode id=2241 lang=python3
#
# [2241] Design an ATM Machine
#

# @lc code=start
from typing import List


class ATM:

    def __init__(self):
        self.bank = [0, 0, 0, 0, 0]
        self.notes = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5): self.bank[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        result = [0, 0, 0, 0, 0]
        for i in range(4, -1, -1):
            toTake = min(self.bank[i], amount // self.notes[i])
            result[i] += toTake
            amount -= toTake * self.notes[i]
        if amount > 0: 
            return [-1]
        else:
            for i in range(5): self.bank[i] -= result[i]
            return result



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
# @lc code=end

