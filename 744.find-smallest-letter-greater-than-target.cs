/*
 * @lc app=leetcode id=744 lang=csharp
 *
 * [744] Find Smallest Letter Greater Than Target
 */

// @lc code=start
using System;
using System;

public class Solution {
    public char NextGreatestLetter(char[] letters, char target) {
        int i = BisectRight(letters, target);
        return letters[i % letters.Length];
    }

    private int BisectRight(char[] letters, char target) {
        int left = 0;
        int right = letters.Length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (letters[mid] > target)
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }
}

// @lc code=end

