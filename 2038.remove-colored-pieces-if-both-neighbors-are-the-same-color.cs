/*
 * @lc app=leetcode id=2038 lang=csharp
 *
 * [2038] Remove Colored Pieces if Both Neighbors are the Same Color
 */

// @lc code=start
public class Solution {
    public bool WinnerOfGame(string colors) {
        colors = "C" + colors + "C";
        int[] count = new int[2];
        int consec = 0;
        char last = ' ';
        
        foreach (char color in colors) {
            if (color != last) {
                if (last == 'A') {
                    count[0] -= Math.Min(consec, 2);
                }
                else if (last == 'B') {
                    count[1] -= Math.Min(consec, 2);
                }
                consec = 1;
            }
            else {
                consec++;
            }
            
            if (color == 'A') {
                count[0]++;
            }
            else if (color == 'B') {
                count[1]++;
            }
            
            last = color;
        }
        
        return count[0] > count[1];
    }
}

// @lc code=end

