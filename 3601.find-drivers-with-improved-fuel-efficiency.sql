--
-- @lc app=leetcode id=3601 lang=mysql
--
-- [3601] Find Drivers with Improved Fuel Efficiency
--

-- @lc code=start
# Write your MySQL query statement below
WITH t1 AS(
    SELECT
        drivers.driver_id,
        drivers.driver_name,
        AVG(trips.distance_km / trips.fuel_consumed) AS first_half_avg
    FROM
        drivers JOIN trips ON drivers.driver_id = trips.driver_id
    WHERE MONTH(trips.trip_date) BETWEEN 1 AND 6
    GROUP BY drivers.driver_id
), t2  AS (
    SELECT
        drivers.driver_id,
        drivers.driver_name,
        AVG(trips.distance_km / trips.fuel_consumed) AS second_half_avg
    FROM
        drivers JOIN trips ON drivers.driver_id = trips.driver_id
    WHERE MONTH(trips.trip_date) BETWEEN 7 AND 12
    GROUP BY drivers.driver_id
)
SELECT
    t1.driver_id,
    t1.driver_name,
    ROUND(t1.first_half_avg, 2) AS first_half_avg,
    ROUND(t2.second_half_avg, 2) AS second_half_avg,
    ROUND(t2.second_half_avg - t1.first_half_avg, 2) AS efficiency_improvement
FROM
    t1 JOIN t2 ON t1.driver_id = t2.driver_id
WHERE
    t2.second_half_avg > t1.first_half_avg
ORDER BY efficiency_improvement DESC, t1.driver_name ASC;
-- @lc code=end

