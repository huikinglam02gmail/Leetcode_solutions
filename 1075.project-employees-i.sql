--
-- @lc app=leetcode id=1075 lang=mysql
--
-- [1075] Project Employees I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT Project.project_id, ROUND(AVG(Employee.experience_years), 2) AS average_years
FROM Project JOIN Employee ON Project.employee_id = Employee.employee_id
GROUP BY Project.project_id
-- @lc code=end

