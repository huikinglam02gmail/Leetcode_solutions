--
-- @lc app=leetcode id=550 lang=mysql
--
-- [550] Game Play Analysis IV
--

-- @lc code=start
# Write your MySQL query statement below

WITH diffRankTable AS
(
	SELECT player_id,
	event_date - LAG(event_date, 1) OVER 
    (
        PARTITION BY player_id 
        ORDER BY event_date
    ) AS difference, 
	RANK() OVER 
    (
        PARTITION BY player_id 
        ORDER BY event_date
    ) AS rowRank
	FROM Activity
),
countTable AS
(
	SELECT COUNT(DISTINCT(player_id)) as all_players
	FROM Activity
)

SELECT IFNULL(ROUND(COUNT(diffRankTable.player_id) / countTable.all_players,2), 0) AS fraction
FROM diffRankTable
JOIN countTable
WHERE diffRankTable.rowRank = 2
AND diffRankTable.difference = 1

-- @lc code=end

