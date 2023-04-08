--
-- @lc app=leetcode id=1164 lang=mysql
--
-- [1164] Product Price at a Given Date
--

-- @lc code=start
# Write your MySQL query statement below
SELECT tbl.product_id, tbl.price
FROM
(
    SELECT product_id, new_price AS price,
    RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rnk
    FROM Products
    WHERE change_date <= "2019-08-16"
) AS tbl 
WHERE tbl.rnk = 1
UNION
SELECT tbl2.product_id, 10 AS price
FROM
(
    SELECT product_id, MIN(change_date) AS chgDate
    FROM Products
    GROUP BY product_id
) AS tbl2
WHERE tbl2.chgDate > "2019-08-16"

-- @lc code=end

