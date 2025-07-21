--
-- @lc app=leetcode id=3617 lang=mysql
--
-- [3617] Find Students with Study Spiral Pattern
--

-- @lc code=start
# Write your MySQL query statement below
WITH Ordered_Sessions AS (
  SELECT
    student_id,
    subject,
    session_date,
    hours_studied,
    ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY session_date) AS date_rank
  FROM
    study_sessions
), Session_With_Gaps AS (
  SELECT
    student_id,
    subject,
    hours_studied,
    date_rank,
    DATEDIFF(
      session_date,
      LAG(session_date) OVER (PARTITION BY student_id ORDER BY session_date)) AS gap
  FROM
    Ordered_Sessions
), Consecutive_Block AS (
  SELECT
    student_id,
    subject,
    hours_studied,
    date_rank,
    gap
  FROM
    Session_With_Gaps
  WHERE
    gap IS NULL OR
    gap <= 2
), Pattern_Candidates AS (
  SELECT
    student_id,
    COUNT(*) AS total_sessions,
    COUNT(DISTINCT subject) AS cycle_length,
    SUM(hours_studied) AS total_study_hours
  FROM
    Consecutive_Block
  GROUP BY
    student_id
    HAVING total_sessions >= cycle_length * 2 AND cycle_length >= 3
)
SELECT
  S.student_id AS student_id,
  S.student_name AS student_name,
  S.major AS major,
  P.cycle_length AS cycle_length,
  P.total_study_hours AS total_study_hours
FROM
  Pattern_Candidates AS P
    JOIN students AS S ON S.student_id = P.student_id
ORDER BY
  P.cycle_length DESC,
  P.total_study_hours DESC;
-- @lc code=end

