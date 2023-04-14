--
-- @lc app=leetcode id=1204 lang=mysql
--
-- [1204] Last Person to Fit in the Bus
--

-- @lc code=start
# Write your MySQL query statement below
SELECT tbl.person_name FROM
(
   SELECT
    turn,
    person_name,
    weight, 
    SUM(weight) OVER (ORDER BY turn) AS Total_weight
    FROM Queue 
) AS tbl
WHERE tbl.Total_weight <= 1000
ORDER BY tbl.turn DESC
LIMIT 1


-- @lc code=end

