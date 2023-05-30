--
-- @lc app=leetcode id=1731 lang=mysql
--
-- [1731] The Number of Employees Which Report to Each Employee
--

-- @lc code=start
# Write your MySQL query statement below
SELECT t3.employee_id, t3.name, COUNT(t3.subordinate_id) AS reports_count, ROUND(AVG(subordinate_age),0) AS average_age
FROM
(
    SELECT t1.employee_id, t1.name, t2.employee_id AS subordinate_id, t2.age AS subordinate_age
    FROM Employees AS t1 JOIN Employees AS t2 ON t2.reports_to = t1.employee_id
) AS t3
GROUP BY t3.employee_id
ORDER BY t3.employee_id
-- @lc code=end
