--
-- @lc app=leetcode id=3374 lang=mysql
--
-- [3374] First Letter Capitalization II
--

-- @lc code=start
# Write your MySQL query statement below
select
    content_id,
    content_text original_text,
    substr(regexp_replace(doubled_content_text, regex, "$1"), 1, char_length(content_text)) converted_text
from (
    select
        content_id,
        content_text,
        concat(lcase(content_text), ucase(content_text)) doubled_content_text,
        concat("(?<=[ -]|^)[a-z](?=.{", char_length(content_text) - 1, "}([a-z]))") regex
    from user_content
) temp
-- @lc code=end

