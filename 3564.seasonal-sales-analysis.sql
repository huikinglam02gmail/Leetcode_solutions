--
-- @lc app=leetcode id=3564 lang=mysql
--
-- [3564] Seasonal Sales Analysis
--

-- @lc code=start
# Write your MySQL query statement below
WITH seasonal_sales AS (
    SELECT
        CASE
            WHEN MONTH(sale_date) IN (12, 1, 2) THEN 'Winter'
            WHEN MONTH(sale_date) IN (3, 4, 5) THEN 'Spring'
            WHEN MONTH(sale_date) IN (6, 7, 8) THEN 'Summer'
            ELSE 'Fall'
        END AS season,
        products.category AS category,
        sales.quantity AS quantity,
        sales.quantity * sales.price AS revenue
    FROM sales INNER JOIN products ON sales.product_id = products.product_id
), allCategorySeasonal_sales AS (
    SELECT
        season,
        category,
        SUM(quantity) AS total_quantity,
        SUM(revenue) AS total_revenue
    FROM seasonal_sales
    GROUP BY season, category
    ORDER BY season ASC, total_quantity DESC, total_revenue DESC
), ranked_sales AS (
    SELECT *,
        RANK() OVER (PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC) AS ranking
    FROM allCategorySeasonal_sales
)
SELECT season, category, total_quantity, total_revenue FROM ranked_sales
WHERE ranking = 1;
-- @lc code=end

