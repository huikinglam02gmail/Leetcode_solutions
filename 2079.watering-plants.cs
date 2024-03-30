/*
 * @lc app=leetcode id=2079 lang=csharp
 *
 * [2079] Watering Plants
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    Just simulation
    */
    public int WateringPlants(int[] plants, int capacity) {
        int result = 0;
        int curCapacity = capacity;
        for (int i = 0; i < plants.Length; i++) {
            if (curCapacity < plants[i]) {
                result += 2 * i;
                curCapacity = capacity;
            }
            curCapacity -= plants[i];
            result += 1;
        }
        return result;
    }
}

// @lc code=end

