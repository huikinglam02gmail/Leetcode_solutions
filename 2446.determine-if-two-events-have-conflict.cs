/*
 * @lc app=leetcode id=2446 lang=csharp
 *
 * [2446] Determine if Two Events Have Conflict
 */

// @lc code=start
public class Solution {
    public bool HaveConflict(string[] event1, string[] event2) {
        int start1 = 0;
        int end1 = 0;
        int start2 = 0;
        int end2 = 0;
        start1 += Int32.Parse(event1[0].Substring(0,2))*60;
        start1 += Int32.Parse(event1[0].Substring(3,2));
        end1 += Int32.Parse(event1[1].Substring(0,2))*60;
        end1 += Int32.Parse(event1[1].Substring(3,2));
        start2 += Int32.Parse(event2[0].Substring(0,2))*60;
        start2 += Int32.Parse(event2[0].Substring(3,2));
        end2 += Int32.Parse(event2[1].Substring(0,2))*60;
        end2 += Int32.Parse(event2[1].Substring(3,2));
        if (start1 <= start2)
        {
            return end1 >= start2;
        }
        else
        {
            return end2 >= start1;
        }
    }
}
// @lc code=end

