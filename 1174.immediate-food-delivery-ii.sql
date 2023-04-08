--
-- @lc app=leetcode id=1174 lang=mysql
--
-- [1174] Immediate Food Delivery II
--

-- @lc code=start
# Write your MySQL query statement below
SELECT ROUND(100*COUNT(tbl.customer_id) / 
    (
        SELECT COUNT(DISTINCT(customer_id))
        FROM Delivery
    )
    , 2) AS 'immediate_percentage'
FROM
(
	SELECT customer_id, order_date, customer_pref_delivery_date,
	RANK() OVER (PARTITION BY customer_id ORDER BY order_date) AS rnk
	FROM Delivery
) AS tbl
WHERE tbl.rnk = 1 AND order_date = customer_pref_delivery_date
-- @lc code=end

