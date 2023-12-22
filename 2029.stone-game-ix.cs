/*
 * @lc app=leetcode id=2029 lang=csharp
 *
 * [2029] Stone Game IX
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    Firstly, notice in this game, 1 behaves the same as 4, 7...
    Just need to record occurrence of the modulo 3
    We then separate into two scenarios in which there is even or odd occurrences of mod0:
    So we just need to simulate
    */
    private bool Game(int mod0, int mod1, int mod2, int S, bool AliceSturn) {
        if (mod0 == 0 && mod1 == 0 && mod2 == 0) return false;
        if (S == 1) {
            if (mod1 > 0) return Game(mod0, mod1 - 1, mod2, 2, !AliceSturn);
            else if (mod0 > 0) return Game(mod0 - 1, mod1, mod2, 1, !AliceSturn);
            else return !AliceSturn;
        } else {
            if (mod2 > 0) return Game(mod0, mod1, mod2 - 1, 1, !AliceSturn);
            else if (mod0 > 0) return Game(mod0 - 1, mod1, mod2, 2, !AliceSturn);
            else return !AliceSturn;
        }
    }

    public bool StoneGameIX(int[] stones) {
        int[] counts = new int[3];
        foreach (int stone in stones) {
            counts[stone % 3] += 1;
        }

        return (counts[1] > 0 && Game(counts[0], counts[1] - 1, counts[2], 1, false)) || 
               (counts[2] > 0 && Game(counts[0], counts[1], counts[2] - 1, 2, false));
    }
}

// @lc code=end

