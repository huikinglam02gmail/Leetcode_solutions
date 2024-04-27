/*
 * @lc app=leetcode id=514 lang=csharp
 *
 * [514] Freedom Trail
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    Use a hash table to store the indices of characters inside the ring
    Use a 2D array to store the minimum steps to finish typing the current key
    Enumerate the minimum of all possible steps from different starts to a certain spot
    To go from index i to j, minimum step = min(abs(i - j), l_r - abs)
    */
    public int FindRotateSteps(string ring, string key) {
        List<int>[] hashRing = new List<int>[26];
        for (int i = 0; i < 26; i++) {
            hashRing[i] = new List<int>();
        }

        for (int i = 0; i < ring.Length; i++) {
            hashRing[ring[i] - 'a'].Add(i);
        }

        int l_r = ring.Length;
        int[][] steps = new int[key.Length][];
        for (int i = 0; i < key.Length; i++) {
            steps[i] = new int[l_r];
            for (int j = 0; j < l_r; j++) {
                steps[i][j] = int.MaxValue;
            }
        }

        List<int> starts = new List<int>() {0};
        for (int i = 0; i < key.Length; i++) {
            List<int> ends = hashRing[key[i] - 'a'];
            foreach (int end in ends) {
                foreach (int start in starts) {
                    if (i == 0) {
                        steps[i][end] = Math.Min(steps[i][end], 1 + Math.Min(Math.Abs(start - end), l_r - Math.Abs(start - end)));
                    } else {
                        steps[i][end] = Math.Min(steps[i][end], steps[i - 1][start] + 1 + Math.Min(Math.Abs(start - end), l_r - Math.Abs(start - end)));
                    }
                }
            }
            starts = ends;
        }

        int minSteps = int.MaxValue;
        foreach (int step in steps[key.Length - 1]) {
            minSteps = Math.Min(minSteps, step);
        }
        return minSteps;
    }
}

// @lc code=end

