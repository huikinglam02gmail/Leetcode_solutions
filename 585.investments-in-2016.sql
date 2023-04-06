--
-- @lc app=leetcode id=585 lang=mysql
--
-- [585] Investments in 2016
--

-- @lc code=start
# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM
(SELECT tiv_2016,
COUNT(*) OVER (PARTITION BY tiv_2015) AS count1, 
COUNT(*) OVER (PARTITION BY lat, lon) AS count2
FROM Insurance
) AS TABLE2
WHERE count1 >= 2 AND count2 = 1
-- @lc code=end

