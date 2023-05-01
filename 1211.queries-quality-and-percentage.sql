--
-- @lc app=leetcode id=1211 lang=mysql
--
-- [1211] Queries Quality and Percentage
--

-- @lc code=start
# Write your MySQL query statement below
SELECT TBL.query_name, ROUND(AVG(TBL.Quality), 2) AS quality, 
ROUND(SUM(CASE WHEN (TBL.Rating < 3) THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS poor_query_percentage
FROM 
(SELECT query_name, rating / position AS Quality, rating AS Rating
FROM Queries) AS TBL
GROUP BY TBL.query_name
-- @lc code=end

