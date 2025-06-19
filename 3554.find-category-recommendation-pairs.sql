--
-- @lc app=leetcode id=3554 lang=mysql
--
-- [3554] Find Category Recommendation Pairs
--

-- @lc code=start
# Write your MySQL query statement below
WITH userID_category AS (
    SELECT ProductPurchases.user_id AS user_id, ProductInfo.category AS category
    FROM ProductPurchases INNER JOIN ProductInfo
    ON ProductPurchases.product_id = ProductInfo.product_id
), comparisons AS (
    SELECT
        a.category AS category1,
        b.category AS category2,
        COUNT(DISTINCT a.user_id) AS customer_count
    FROM userID_category a
    JOIN userID_category b
    ON a.category < b.category AND a.user_id = b.user_id
    GROUP BY a.category, b.category
    having COUNT(DISTINCT a.user_id) >= 3
)
SELECT
    category1,
    category2,
    customer_count
FROM comparisons
ORDER BY customer_count DESC, category1 ASC, category2 ASC 

-- @lc code=end

