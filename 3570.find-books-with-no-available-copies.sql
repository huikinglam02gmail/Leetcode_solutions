--
-- @lc app=leetcode id=3570 lang=mysql
--
-- [3570] Find Books with No Available Copies
--

-- @lc code=start
# Write your MySQL query statement below
WITH book_availability AS (
    SELECT
        book_id,
        COUNT(record_id) AS current_borrowers
    FROM borrowing_records
    WHERE return_date IS NULL 
    GROUP BY book_id
)
SELECT 
    library_books.book_id, 
    library_books.title, 
    library_books.author, 
    library_books.genre, 
    library_books.publication_year, 
    book_availability.current_borrowers
FROM library_books JOIN book_availability ON library_books.book_id = book_availability.book_id
WHERE book_availability.current_borrowers = library_books.total_copies
ORDER BY book_availability.current_borrowers DESC, library_books.title ASC;
-- @lc code=end

