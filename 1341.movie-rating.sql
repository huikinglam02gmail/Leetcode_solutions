--
-- @lc app=leetcode id=1341 lang=mysql
--
-- [1341] Movie Rating
--

-- @lc code=start
# Write your MySQL query statement below
WITH mR AS (SELECT Users.name, Movies.title, MovieRating.rating, EXTRACT(MONTH FROM MovieRating.created_at) AS month, EXTRACT(YEAR FROM MovieRating.created_at) AS year FROM MovieRating JOIN Movies ON MovieRating.movie_id = Movies.movie_id JOIN Users ON MovieRating.user_id = Users.user_id)
(SELECT mRCount.name AS results 
FROM (
        SELECT mR.name, COUNT(mR.name) AS count 
        FROM mR 
        GROUP BY mR.name
    ) AS mRCount 
ORDER BY mRCount.count DESC, mRCount.name ASC LIMIT 1)
UNION
(SELECT mRating.title AS results
FROM (
        SELECT mR.title, AVG(mR.rating) AS rating 
        FROM mR 
        WHERE mR.month = 2 AND mR.year = 2020 
        GROUP BY mR.title
    ) AS mRating 
ORDER BY mRating.rating DESC, mRating.title ASC LIMIT 1)

-- @lc code=end

