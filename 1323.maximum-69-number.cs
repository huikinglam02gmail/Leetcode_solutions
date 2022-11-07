/*
 * @lc app=leetcode id=1323 lang=csharp
 *
 * [1323] Maximum 69 Number
 */

// @lc code=start
public class Solution 
{
    public int Maximum69Number (int num) 
    {
        string numDigit = num.ToString();
        for (int i = 0; i < numDigit.Length; i++)
        {
            if (numDigit[i] == '6')
            {
                return Int32.Parse(numDigit.Substring(0,i) + '9' + numDigit.Substring(i+1,numDigit.Length-i-1));
            }
        }
        return num;    
    }
}
// @lc code=end

