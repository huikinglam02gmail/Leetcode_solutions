/*
 * @lc app=leetcode id=1441 lang=csharp
 *
 * [1441] Build an Array With Stack Operations
 */

// @lc code=start
public class Solution 
{
    public IList<string> BuildArray(int[] target, int n) 
    {
        List<string> result = new List<string>();
        int j = 0;
        for (int i = 1; i < n+1; i++)
        {
            result.Add("Push");
            if (i == target[j])
            {
                j += 1;
            }
            else
            {
                result.Add("Pop");
            }
            if (j == target.Length)
            {
                return result;
            }
        }
        return result;   
    }
}
// @lc code=end

