--
-- @lc app=leetcode id=3465 lang=mysql
--
-- [3465] Find Products with Valid Serial Numbers
--

-- @lc code=start
# Write your MySQL query statement below
SELECT product_id, product_name, description FROM Products
WHERE description REGEXP 'SN[0-9]{4}-[0-9]{4}\\b'
ORDER BY product_id
-- @lc code=end

