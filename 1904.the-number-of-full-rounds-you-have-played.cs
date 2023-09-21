/*
 * @lc app=leetcode id=1904 lang=csharp
 *
 * [1904] The Number of Full Rounds You Have Played
 */

// @lc code=start
public class Solution {
    /*
     * Convert the times to mins
     * if logout < login, + 24 * 60 to it
     * Then // 15
     */
    public int CeilDiv(int a, int b) {
        return (a + b - 1) / b;
    }

    public int NumberOfRounds(string loginTime, string logoutTime) {
        int login = int.Parse(loginTime.Substring(0, 2)) * 60 + int.Parse(loginTime.Substring(3));
        int logout = int.Parse(logoutTime.Substring(0, 2)) * 60 + int.Parse(logoutTime.Substring(3));

        if (login > logout) {
            logout += 24 * 60;
        }

        return Math.Max(0, logout / 15 - CeilDiv(login, 15));
    }
}

// @lc code=end

