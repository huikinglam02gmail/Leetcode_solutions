--
-- @lc app=leetcode id=602 lang=mysql
--
-- [602] Friend Requests II: Who Has the Most Friends
--

-- @lc code=start
# Write your MySQL query statement below
SELECT temp.id, COUNT(temp.id) AS num
FROM (
  SELECT requester_id AS id FROM RequestAccepted
  UNION ALL
  SELECT accepter_id AS id FROM RequestAccepted
) AS temp
GROUP BY temp.id
ORDER BY COUNT(temp.id) DESC LIMIT 1
-- @lc code=end

