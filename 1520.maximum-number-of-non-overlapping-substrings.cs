/*
 * @lc app=leetcode id=1520 lang=csharp
 *
 * [1520] Maximum Number of Non-Overlapping Substrings
 */

// @lc code=start
public class Solution 
{
    public int bisectLeft(int[] nums, int target)
    {
        int left = 0;
        int right = nums.Length;

        while (left < right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return left;
    }

    public int bisectRight(int[] nums, int target)
    {
        int left = 0;
        int right = nums.Length;

        while (left < right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] <= target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return left;
    }

    public IList<string> MaxNumOfSubstrings(string s) 
    {
        Dictionary<char, List<int>> appear = new Dictionary<char, List<int>>();
        int n = s.Length;
        for (int i = 0; i < n; i++)
        {
            if (!appear.ContainsKey(s[i]))
            {
                appear[s[i]] = new List<int>();
            }
            appear[s[i]].Add(i);
        }
        List<char> keys = new List<char>(appear.Keys);
        List<int[]> candidates = new List<int[]>();
        List<string> result = new List<string>();

        foreach (char key1 in keys)
        {
            int n1 = appear[key1].Count;
            int start = appear[key1][0];
            int end = appear[key1][n1-1];
            bool foundSubstring = false;
            bool  impossible = false;
            while (!impossible && !foundSubstring)
            {
                int count = 0;
                foreach (char key2 in keys)
                {
                    int n2 = appear[key2].Count;
                    indStart = bisectLeft(appear[key2], start);
                    indEnd = bisectLeft(appear[key2], end);
                    if (indStart != indEnd && appear[key2][0] < start)
                    {
                        impossible = true;
                        break;
                    }
                    else if (indStart != indEnd && appear[key2][n2-1] > end)
                    {
                        end = appear[key2][n2 - 1];
                        break;
                    }
                    else
                    {
                        count++;
                    }
                }
                if (count == keys.Count)
                {
                    foundSubstring = true;
                }
            }
            if (!impossible && foundSubstring)
            {
                candidates.Add(new int[2]{end, start});
            }
        }
        candidates = candidates.OrderBy(x => x[0]);
        int lastEnd = -1;
        foreach (int[] interval in candidates)
        {
            if (interval[1] > lastEnd)
            {
                List.Add(s.Substring(start, end - start));
                lastEnd = end;
            }
        }
        return result;
    }
}
// @lc code=end

