--
-- @lc app=leetcode id=3580 lang=mysql
--
-- [3580] Find Consistently Improving Employees
--

-- @lc code=start
# Write your MySQL query statement below
WITH thrice_employees AS (
    SELECT employee_id
    FROM performance_reviews
    GROUP BY employee_id
    HAVING COUNT(review_date) >= 3
), mergedTable AS (
    SELECT employees.employee_id, 
        employees.name,
        LAG(performance_reviews.rating, 1) OVER (PARTITION BY employees.employee_id ORDER BY performance_reviews.review_date ASC) AS previous_rating,
        LAG(performance_reviews.rating, 2) OVER (PARTITION BY employees.employee_id ORDER BY performance_reviews.review_date) AS second_previous_rating,
        performance_reviews.rating AS latest_rating,
        RANK() OVER (PARTITION BY employees.employee_id ORDER BY performance_reviews.review_date DESC) AS latest_rank
FROM employees JOIN performance_reviews ON employees.employee_id = performance_reviews.employee_id
WHERE employees.employee_id IN (SELECT thrice_employees.employee_id FROM thrice_employees)
)
SELECT 
    employee_id, 
    name,
    latest_rating - second_previous_rating AS improvement_score
FROM mergedTable
WHERE latest_rank = 1 AND 
      latest_rating > previous_rating AND 
      previous_rating > second_previous_rating
ORDER BY improvement_score DESC, name ASC;

-- @lc code=end

