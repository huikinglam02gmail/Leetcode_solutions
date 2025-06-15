--
-- @lc app=leetcode id=3497 lang=mysql
--
-- [3497] Analyze Subscription Conversion 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 
user_id,
ROUND(SUM(IF(activity_type = 'free_trial', 1, 0) * activity_duration) / SUM(IF(activity_type = 'free_trial', 1, 0)), 2) AS trial_avg_duration,
ROUND(SUM(IF(activity_type = 'paid', 1, 0) * activity_duration) / SUM(IF(activity_type = 'paid', 1, 0)), 2) AS paid_avg_duration
FROM
UserActivity
GROUP BY user_id
HAVING SUM(IF(activity_type = 'paid', 1, 0)) > 0
ORDER BY user_id;
-- @lc code=end

