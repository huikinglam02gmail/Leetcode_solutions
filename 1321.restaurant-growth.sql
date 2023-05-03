--
-- @lc app=leetcode id=1321 lang=mysql
--
-- [1321] Restaurant Growth
--

-- @lc code=start
# Write your MySQL query statement below
SELECT TBL1.visited_on AS visited_on, SUM(TBL2.daySum) AS amount,
ROUND(AVG(TBL2.daySum),2) AS average_amount
FROM
(
    SELECT visited_on, SUM(amount) AS daySum 
    FROM Customer 
    GROUP BY visited_on
) AS TBL1 JOIN
(   
    SELECT visited_on, SUM(amount) AS daySum
    FROM Customer 
    GROUP BY visited_on
) AS TBL2
WHERE DATEDIFF(TBL1.visited_on, TBL2.visited_on) BETWEEN 0 AND 6
GROUP BY TBL1.visited_on
HAVING COUNT(TBL2.visited_on) = 7

-- @lc code=end

