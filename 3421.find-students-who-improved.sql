--
-- @lc app=leetcode id=3421 lang=mysql
--
-- [3421] Find Students Who Improved
--

-- @lc code=start
# Write your MySQL query statement below
WITH RankedScore AS (
    SELECT 
        student_id,
        subject,
        score,
        ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date ASC) AS earliest_rank,
        ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS latest_rank
    FROM Scores
)
SELECT 
    rs1.student_id,
    rs1.subject,
    rs1.score AS first_score,
    rs2.score AS latest_score
FROM RankedScore rs1
JOIN RankedScore rs2 ON rs1.student_id = rs2.student_id AND rs1.subject = rs2.subject
WHERE 
    rs1.earliest_rank = 1 AND 
    rs2.latest_rank = 1 AND 
    rs2.score > rs1.score
ORDER BY rs1.student_id, rs1.subject;

-- @lc code=end

