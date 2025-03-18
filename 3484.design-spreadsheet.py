#
# @lc app=leetcode id=3484 lang=python3
#
# [3484] Design Spreadsheet
#

# @lc code=start
class Spreadsheet:

    def __init__(self, rows: int):
        self.hashTable = {}

    def setCell(self, cell: str, value: int) -> None:
        self.hashTable[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.hashTable: self.hashTable.pop(cell)

    def getValue(self, formula: str) -> int:
        formulaSplit = formula.split('+')
        values = 0
        if formulaSplit[0][1].isalpha(): values += self.hashTable.get(formulaSplit[0][1:], 0)
        else: values += int(formulaSplit[0][1:])
        if formulaSplit[1][0].isalpha(): values += self.hashTable.get(formulaSplit[1], 0)
        else: values += int(formulaSplit[1])
        return values


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
# @lc code=end

