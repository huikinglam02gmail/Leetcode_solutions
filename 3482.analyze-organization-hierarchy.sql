--
-- @lc app=leetcode id=3482 lang=mysql
--
-- [3482] Analyze Organization Hierarchy
--

-- @lc code=start
# Write your MySQL query statement below
WITH RECURSIVE level_cte AS (
  SELECT employee_id, manager_id, 1 AS level, salary FROM Employees
  UNION ALL
  SELECT level_cte.employee_id, Employees.manager_id, level + 1, level_cte.salary
    FROM level_cte JOIN Employees on Employees.employee_id = level_cte.manager_id
), teamWithBudgetExcludingManager AS (
    SELECT 
        manager_id AS employee_id, 
        COUNT(*) AS team_size, 
        SUM(salary) AS budget 
    FROM level_cte 
    WHERE manager_id IS NOT NULL 
    GROUP BY manager_id    
), employee_with_level AS (
    SELECT Employees.employee_id, Employees.employee_name, Employees.salary, b.level FROM Employees, 
    (
        SELECT employee_id, level FROM level_cte WHERE manager_id IS NULL
    ) b 
    WHERE Employees.employee_id = b.employee_id
)
SELECT 
    employee_with_level.employee_id, 
    employee_with_level.employee_name, 
    employee_with_level.level, 
    COALESCE(teamWithBudgetExcludingManager.team_size, 0) AS team_size, 
    employee_with_level.salary + COALESCE(teamWithBudgetExcludingManager.budget, 0) AS budget
FROM employee_with_level LEFT JOIN teamWithBudgetExcludingManager ON teamWithBudgetExcludingManager.employee_id = employee_with_level.employee_id
ORDER BY level ASC, budget DESC, employee_name ASC;

-- @lc code=end

