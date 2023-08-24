/*
 * @lc app=leetcode id=68 lang=csharp
 *
 * [68] Text Justification
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> FullJustify(string[] words, int maxWidth) {
        int j = 0;
        int wordLengthAccumulated = 0;
        List<string> result = new List<string>();
        int n = words.Length;
        string row;

        for (int i = 0; i < n; i++) {
            if (wordLengthAccumulated + i - j + words[i].Length > maxWidth) {
                row = words[j];
                int remainingEmptySpace = maxWidth - wordLengthAccumulated;
                wordLengthAccumulated -= words[j].Length;
                j++;
                
                if (i == j) {
                    row += new string(' ', remainingEmptySpace);
                } else {
                    int shortest = remainingEmptySpace / (i - j);
                    while (j < i) {
                        if (remainingEmptySpace % (i - j) > 0) {
                            row += new string(' ', shortest + 1);
                            remainingEmptySpace -= shortest + 1;
                        } else {
                            row += new string(' ', shortest);
                            remainingEmptySpace -= shortest;
                        }
                        row += words[j];
                        wordLengthAccumulated -= words[j].Length;
                        j++;
                    }
                }
                
                result.Add(row);
            }
            
            wordLengthAccumulated += words[i].Length;
        }
        
        row = "";
        
        while (wordLengthAccumulated > 0) {
            row += words[j];
            wordLengthAccumulated -= words[j].Length;
            
            if (wordLengthAccumulated > 0) {
                row += " ";
                j++;
            }
        }
        
        while (row.Length < maxWidth) {
            row += " ";
        }
        
        result.Add(row);
        
        return result;
    }
}

// @lc code=end

