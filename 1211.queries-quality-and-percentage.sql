--
-- @lc app=leetcode id=1211 lang=mysql
--
-- [1211] Queries Quality and Percentage
--

-- @lc code=start
# Write your MySQL query statement below
SELECT TBL.query_name, ROUND(AVG(TBL.Quality), 2) AS quality, COUNT(DTBL.Quality < 3) / COUNT(TBL.Quality) * 100 AS poor_query_percentage
FROM 
(SELECT query_name, rating / position AS Quality
FROM Queries) AS TBL
GROUP BY TBL.query_name
-- @lc code=end

