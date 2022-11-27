/*
 * @lc app=leetcode id=1496 lang=csharp
 *
 * [1496] Path Crossing
 */

// @lc code=start
public class Solution 
{
    public bool IsPathCrossing(string path) 
    {
        HashSet<Tuple<int, int>> seen = new HashSet<Tuple<int, int>>();
        int x = 0;
        int y = 0;
        seen.Add(new Tuple<int,int> (x, y));
        foreach (char c in path)
        {
            if (c == 'N')
            {
                y++;
            }
            else if (c == 'E')
            {
                x++;
            }
            else if (c == 'S')
            {
                y--;
            }
            else
            {
                x--;
            }
            if (seen.Contains(new Tuple<int,int> (x, y)))
            {
                return true;
            }
            else
            {
                seen.Add(new Tuple<int,int> (x, y));
            }
        }
        return false;  
    }
}
// @lc code=end

