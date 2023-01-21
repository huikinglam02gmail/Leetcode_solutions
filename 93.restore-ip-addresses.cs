/*
 * @lc app=leetcode id=93 lang=csharp
 *
 * [93] Restore IP Addresses
 */

// @lc code=start
public class Solution 
{
    public bool validIP(List<string> arr)
    {
        for (int i = 0; i < 4; i++)
        {
            if ((arr[i].Length > 1 && arr[i][0] == '0') || arr[i].Length > 3 || Int32.Parse(arr[i]) > 255)
            {
                return false;
            }
        }
        return true;
    }
    public IList<string> RestoreIpAddresses(string s) 
    {
        List<string> result = new List<string>();
        if (s.Length >= 4)
        {
            List<string> arr = new List<string>();
            for (int i = 1; i < s.Length - 2; i++)
            {
                arr.Add(s.Substring(0, i));
                for (int j = i + 1; j < s.Length - 1; j++)
                {
                    arr.Add(s.Substring(i, j - i));
                    for (int k = j + 1; k < s.Length; k++)
                    {
                        arr.Add(s.Substring(j, k - j));
                        arr.Add(s.Substring(k));
                        if (validIP(arr))
                        {
                            result.Add(string.Join('.', arr.ToArray()));
                        }
                        arr.RemoveAt(arr.Count - 1);
                        arr.RemoveAt(arr.Count - 1);
                    }
                    arr.RemoveAt(arr.Count - 1);
                }
                arr.RemoveAt(arr.Count - 1);
            }
        }
        return result;    
    }
}
// @lc code=end

