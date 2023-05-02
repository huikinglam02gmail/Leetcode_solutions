--
-- @lc app=leetcode id=1280 lang=mysql
--
-- [1280] Students and Examinations
--

-- @lc code=start
# Write your MySQL query statement below
SELECT Students.student_id, Students.student_name, Subjects.subject_name, COUNT(Examinations.subject_name) as attended_exams
FROM Students JOIN Subjects
LEFT JOIN Examinations ON Students.student_id = Examinations.student_id AND Examinations.subject_name = Subjects.subject_name
GROUP BY Students.student_id, Subjects.subject_name
ORDER BY Students.student_id, Subjects.subject_name

-- @lc code=end

