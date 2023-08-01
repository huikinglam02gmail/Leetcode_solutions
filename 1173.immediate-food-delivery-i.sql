--
-- @lc app=leetcode id=1173 lang=mysql
--
-- [1173] Immediate Food Delivery I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT ROUND(100 * SUM(order_date = customer_pref_delivery_date) / COUNT(*), 2) AS immediate_percentage FROM Delivery;

-- @lc code=end

