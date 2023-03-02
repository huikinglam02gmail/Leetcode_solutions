/*
 * @lc app=leetcode id=443 lang=csharp
 *
 * [443] String Compression
 */

// @lc code=start
public class Solution 
{
    public int Compress(char[] chars) 
    {
        int left = 0;
        int right = 0;
        int n = chars.Length;
        int result = 0;
        while (right < n)
        {
            result++;
            chars[left] = chars[right];
            int count = 0;
            while (right < n && chars[right] == chars[left])
            {
                right++;
                count++;
            }
            left++;
            if (count > 1)
            {
                string diff = count.ToString();
                int lastLeft = left;
                while (left < lastLeft + diff.Length)
                {
                    result++;
                    chars[left] = diff[left - lastLeft];
                    left++; 
                }                
            }
        }
        return result;
    }
}
// @lc code=end

