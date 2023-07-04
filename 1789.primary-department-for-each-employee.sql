--
-- @lc app=leetcode id=1789 lang=mysql
--
-- [1789] Primary Department for Each Employee
--

-- @lc code=start
# Write your MySQL query statement below
SELECT employee_id,
       COALESCE(MAX(CASE WHEN primary_flag='Y' THEN department_id ELSE NULL END), MAX(department_id)) department_id
FROM Employee
GROUP BY employee_id
-- @lc code=end

