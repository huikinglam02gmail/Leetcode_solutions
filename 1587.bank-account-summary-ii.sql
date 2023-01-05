--
-- @lc app=leetcode id=1587 lang=mysql
--
-- [1587] Bank Account Summary II
--

-- @lc code=start
# Write your MySQL query statement below
SELECT Users.name, SUM(Transactions.amount) AS balance
FROM Users INNER JOIN Transactions ON Users.account = Transactions.account
GROUP BY Transactions.account
HAVING SUM(Transactions.amount) > 10000
-- @lc code=end

