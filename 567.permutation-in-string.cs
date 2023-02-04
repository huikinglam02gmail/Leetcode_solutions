/*
 * @lc app=leetcode id=567 lang=csharp
 *
 * [567] Permutation in String
 */

// @lc code=start
public class Solution 
{
    public int checkAppearance(int[] count1, int[] count2)
    {
        int count = 0;
        for (int i = 0; i < 26; i++)
        {
            if (count1[i] > count2[i])
            {
                return -1;
            }
            else if (count1[i] == count2[i])
            {
                count++;
            }
        }
        if (count == 26)
        {
            return 0;
        }
        else
        {
            return 1;
        }
    }

    public bool CheckInclusion(string s1, string s2) 
    {
        if (s2.Length < s1.Length)
        {
            return false;
        }
        else
        {
            int[] seen1 = new int[26];
            int[] seen2 = new int[26];
            int left = 0;
            Array.Fill(seen1, 0);
            Array.Fill(seen2, 0);
            foreach (char c in s1)
            {
                seen1[(int)c - (int)'a']++;
            }

            for (int right = 0; right < s2.Length; right++)
            {
                seen2[(int)s2[right] - (int)'a']++;
                while (checkAppearance(seen1, seen2) == 1)
                {
                    seen2[(int)s2[left] - (int)'a']--;
                    left++;
                }
                if (checkAppearance(seen1, seen2) == 0)
                {
                    return true;
                }
            }
            return false;
        }
    }
}
// @lc code=end

