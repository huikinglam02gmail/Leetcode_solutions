/*
 * @lc app=leetcode id=2849 lang=csharp
 *
 * [2849] Determine if a Cell Is Reachable at a Given Time
 */

// @lc code=start
public class Solution {
    public bool IsReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        int need = Math.Max(Math.Abs(sx - fx), Math.Abs(sy - fy));
        if (need == 0 && t == 1)
            return false;
        return need <= t;
    }
}

// @lc code=end

