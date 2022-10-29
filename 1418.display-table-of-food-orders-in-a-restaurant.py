#
# @lc app=leetcode id=1418 lang=python3
#
# [1418] Display Table of Food Orders in a Restaurant
#

# @lc code=start
class Solution:
    # hash table question
    # Construct the hash table and use (tableNumber, foodItem) as key
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        hashTable = {}
        for customerName,tableNumber,foodItem in orders:
            hashTable[(tableNumber, foodItem)] = hashTable.get((tableNumber, foodItem),0) + 1
        keys, tables, food = hashTable.keys(), set(), set()
        for table, item in keys:
            tables.add(table)
            food.add(item)
        tables = sorted(list(tables), key = lambda x: int(x))
        food = sorted(list(food))
        m, n = len(tables), len(food)
        result = [["" for j in range(n+1)] for i in range(m+1)]
        result[0][0] = "Table"
        for i in range(1, m+1):
            result[i][0] = tables[i-1]
        for j in range(1, n+1):
            result[0][j] = food[j-1]
        for i in range(1,m+1):
            for j in range(1, n+1):
                result[i][j] = str(hashTable.get((tables[i-1],food[j-1]),0))
        return result
# @lc code=end

