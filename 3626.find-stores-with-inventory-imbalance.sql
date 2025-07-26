--
-- @lc app=leetcode id=3626 lang=mysql
--
-- [3626] Find Stores with Inventory Imbalance
--

-- @lc code=start
# Write your MySQL query statement below
WITH storesToInclude AS (
    SELECT stores.store_id, stores.store_name, stores.location, MAX(price) AS max_price, MIN(price) AS min_price
    FROM inventory
    JOIN stores ON inventory.store_id = stores.store_id
    GROUP BY stores.store_id
    HAVING COUNT(DISTINCT product_name) >= 3
), storesWithMaxAndMinPrices AS (
    SELECT storesToInclude.store_id, storesToInclude.store_name, storesToInclude.location, inventory.product_name, inventory.price, inventory.quantity
    FROM storesToInclude JOIN inventory ON (storesToInclude.store_id = inventory.store_id AND inventory.price = storesToInclude.max_price OR inventory.price = storesToInclude.min_price)
)
SELECT s1.store_id, s1.store_name, s1.location, s1.product_name AS most_exp_product, s2.product_name AS cheapest_product, ROUND(s2.quantity / s1.quantity, 2) AS imbalance_ratio
FROM storesWithMaxAndMinPrices s1 JOIN storesWithMaxAndMinPrices s2 ON (s1.store_id = s2.store_id AND s1.price > s2.price)
WHERE s2.quantity > s1.quantity
ORDER BY imbalance_ratio DESC, s1.store_id, s1.store_name ASC;
-- @lc code=end

