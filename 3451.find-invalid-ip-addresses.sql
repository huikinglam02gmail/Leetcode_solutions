--
-- @lc app=leetcode id=3451 lang=mysql
--
-- [3451] Find Invalid IP Addresses
--

-- @lc code=start
# Write your MySQL query statement below
SELECT ip, COUNT(*) AS invalid_count
FROM logs
WHERE 
    LENGTH(ip) - LENGTH(REPLACE(ip, '.', '')) != 3 
    OR ip REGEXP '\\.0[0-9]+|^0[0-9]+'
    OR NOT (
        SUBSTRING_INDEX(ip, '.', 1) REGEXP '^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$' AND
        SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) REGEXP '^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$' AND
        SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', -2), '.', 1) REGEXP '^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$' AND
        SUBSTRING_INDEX(ip, '.', -1) REGEXP '^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$'
    )
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
-- @lc code=end

