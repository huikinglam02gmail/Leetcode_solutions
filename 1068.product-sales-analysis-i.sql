--
-- @lc app=leetcode id=1068 lang=mysql
--
-- [1068] Product Sales Analysis I
--

-- @lc code=start
# Write your MySQL query statement below
SELECT Product.product_name, Sales.year, Sales.price
FROM Product JOIN Sales
ON Sales.product_id = Product.product_id
-- @lc code=end

