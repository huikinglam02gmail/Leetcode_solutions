--
-- @lc app=leetcode id=619 lang=mysql
--
-- [619] Biggest Single Number
--

-- @lc code=start
# Write your MySQL query statement below
SELECT MAX(num) AS num
FROM
(SELECT num, COUNT(num) AS count
FROM MyNumbers
GROUP BY num
HAVING count = 1
) AS TBL

-- @lc code=end

