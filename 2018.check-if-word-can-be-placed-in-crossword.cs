/*
 * @lc app=leetcode id=2018 lang=csharp
 *
 * [2018] Check if Word Can Be Placed In Crossword
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
    There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
    That means we just need to test for each point whether the word can start from there
    */
    public bool PlaceWordInCrossword(char[][] board, string word) {
        int m = board.Length;
        int n = board[0].Length;
        int l = word.Length;
        int[][] proceedDirections = { new int[] { 1, 0 }, new int[] { -1, 0 }, new int[] { 0, 1 }, new int[] { 0, -1 } };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '#') continue; // rule 1
                if (board[i][j] != ' ' && board[i][j] != word[0]) continue; // rule 2

                for (int k = 0; k < 4; k++) {
                    int x = i, y = j, wordPtr = 0;
                    int xPrev = x - proceedDirections[k][0], yPrev = y - proceedDirections[k][1];

                    if (xPrev >= 0 && xPrev < m && yPrev >= 0 && yPrev < n && board[xPrev][yPrev] != '#') continue; // rule 3

                    while (x >= 0 && x < m && y >= 0 && y < n && wordPtr < l) {
                        if (board[x][y] == ' ' || board[x][y] == word[wordPtr]) {
                            x += proceedDirections[k][0];
                            y += proceedDirections[k][1];
                            wordPtr++;
                        } else {
                            break;
                        }
                    }

                    if (wordPtr < l) continue;

                    if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] != '#') continue; // rule 4

                    return true;
                }
            }
        }

        return false;
    }
}

// @lc code=end

