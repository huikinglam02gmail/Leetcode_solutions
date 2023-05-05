--
-- @lc app=leetcode id=1661 lang=mysql
--
-- [1661] Average Time of Process per Machine
--

-- @lc code=start
# Write your MySQL query statement below
WITH
    cteStart AS (SELECT machine_id, AVG(timestamp) AS startTime
    FROM Activity
    WHERE activity_type = 'start'
    GROUP BY machine_id),
    cteEnd AS (SELECT machine_id, AVG(timestamp) AS endTime
    FROM Activity
    WHERE activity_type = 'end'
    GROUP BY machine_id)
SELECT cteEnd.machine_id, ROUND(cteEnd.endTime - cteStart.startTime,3) AS processing_time
FROM cteStart JOIN cteEnd ON cteStart.machine_id = cteEnd.machine_id
-- @lc code=end

