--
-- @lc app=leetcode id=3521 lang=mysql
--
-- [3521] Find Product Recommendation Pairs
--

-- @lc code=start
# Write your MySQL query statement below
WITH AllPurchases AS (
    SELECT
        ProductPurchases.product_id AS product_id,
        ProductPurchases.user_id AS user_id,
        ProductInfo.category AS category
    FROM ProductPurchases JOIN ProductInfo ON ProductPurchases.product_id = ProductInfo.product_id
), ProductPairTable AS( 
    SELECT
        p1.product_id AS product1_id,
        p2.product_id AS product2_id,
        p1.category AS product1_category,
        p2.category AS product2_category,
        COUNT(DISTINCT p1.user_id) AS customer_count
    FROM AllPurchases p1 JOIN AllPurchases p2 ON p1.user_id = p2.user_id
    WHERE p1.product_id < p2.product_id
    GROUP BY p1.product_id, p2.product_id
)
SELECT * FROM ProductPairTable
WHERE customer_count >= 3
ORDER BY customer_count DESC, product1_id ASC, product2_id ASC;
-- @lc code=end

