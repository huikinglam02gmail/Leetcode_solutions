/*
 * @lc app=leetcode id=287 lang=csharp
 *
 * [287] Find the Duplicate Number
 */

// @lc code=start
using System;

public class Solution {
    public int FindDuplicate(int[] nums) {
        int slow = 0, fast = 0;
        bool match = false;

        while (!match) {
            slow = nums[slow];
            fast = nums[fast];
            fast = nums[fast];

            if (nums[slow] == nums[fast]) {
                match = true;
            }
        }

        slow = 0;
        if (nums[slow] != nums[fast]) {
            match = false;

            while (!match) {
                slow = nums[slow];
                fast = nums[fast];

                if (nums[slow] == nums[fast]) {
                    match = true;
                }
            }
        }

        return nums[slow];
    }
}

// @lc code=end

