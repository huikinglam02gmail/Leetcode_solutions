--
-- @lc app=leetcode id=1193 lang=mysql
--
-- [1193] Monthly Transactions I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 
LEFT(trans_date, 7) AS month, 
country, 
COUNT(id) AS trans_count, 
SUM(CASE 
    WHEN state = 'approved' THEN 1 
    ELSE 0 
    END) AS approved_count, 
SUM(amount) AS trans_total_amount, 
SUM(CASE 
    WHEN state = 'approved' THEN amount 
    ELSE 0 
    END) AS approved_total_amount
FROM Transactions
GROUP BY month, country
-- @lc code=end

