--
-- @lc app=leetcode id=570 lang=mysql
--
-- [570] Managers with at Least 5 Direct Reports
--

-- @lc code=start
# Write your MySQL query statement below
SELECT name FROM Employee 
WHERE id IN
(
   SELECT managerId
   FROM Employee
   GROUP BY managerId
   HAVING (COUNT(managerId) >= 5)
)
-- @lc code=end

