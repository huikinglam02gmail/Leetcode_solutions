/*
 * @lc app=leetcode id=1839 lang=csharp
 *
 * [1839] Longest Substring Of All Vowels in Order
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    /*
    This is a sliding window problem.
    Pretty much we can add to the current string the current character
    Since we only have aeiou, we just need to find if the appearance of a, e, i, o and u are sorted.
    If not, any further indices would not be beautiful.
    For example if word = "aeiaaioaaaaeiiiiouuuooaauuaeiu" When we have current valid string to be "aei", and when "a" comes in, we check if "e", "i", "o" and "u" has occurred. If so, pop them.
    */
    public int LongestBeautifulSubstring(string word)
    {
        Dictionary<char, int> vowels = new Dictionary<char, int>
        {
            {'a', 0},
            {'e', 1},
            {'i', 2},
            {'o', 3},
            {'u', 4}
        };

        List<Queue<int>> indices = new List<Queue<int>>(new Queue<int>[5]);
        for (int i = 0; i < 5; i++)
        {
            indices[i] = new Queue<int>();
        }

        int result = 0;
        for (int ind = 0; ind < word.Length; ind++)
        {
            char c = word[ind];
            for (int i = vowels[c] + 1; i < 5; i++)
            {
                while (indices[i].Count > 0)
                {
                    for (int j = 0; j < i; j++)
                    {
                        while (indices[j].Count > 0 && indices[j].Peek() < indices[i].Peek())
                        {
                            indices[j].Dequeue();
                        }
                    }
                    indices[i].Dequeue();
                }
            }
            indices[vowels[c]].Enqueue(ind);
            if (indices.All(x => x.Count > 0))
            {
                result = Math.Max(result, indices.Sum(x => x.Count));
            }
        }
        return result;
    }
}

// @lc code=end

