/*
 * @lc app=leetcode id=950 lang=csharp
 *
 * [950] Reveal Cards In Increasing Order
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] DeckRevealedIncreasing(int[] deck) {
        int n = deck.Length;
        int j = 0;
        int[] result = new int[n];
        Queue<int> dq = new Queue<int>();

        Array.Sort(deck);

        for (int i = 0; i < n; i++) {
            dq.Enqueue(i);
        }

        while (dq.Count >= 2) {
            result[dq.Dequeue()] = deck[j++];
            dq.Enqueue(dq.Dequeue());
        }

        result[dq.Dequeue()] = deck[j];
        return result;
    }
}

// @lc code=end

