--
-- @lc app=leetcode id=1251 lang=mysql
--
-- [1251] Average Selling Price
--

-- @lc code=start
# Write your MySQL query statement below
SELECT TBL.product_id, ROUND( SUM(TBL.units * TBL.price) / SUM(TBL.units),2) AS average_price
FROM 
(SELECT UnitsSold.product_id AS product_id, UnitsSold.units AS units, Prices.price AS price
FROM UnitsSold JOIN Prices
ON UnitsSold.product_id = Prices.product_id
WHERE UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date) AS TBL
GROUP BY TBL.product_id
-- @lc code=end

