/*
 * @lc app=leetcode id=1835 lang=csharp
 *
 * [1835] Find XOR Sum of All Pairs Bitwise AND
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int GetXORSum(int[] arr1, int[] arr2) {
        int numberOfDigits1 = GetNumberOfDigits(arr1);
        int numberOfDigits2 = GetNumberOfDigits(arr2);
        int numberOfDigits = Math.Max(numberOfDigits1, numberOfDigits2);

        if (numberOfDigits1 > numberOfDigits2) {
            SwapArrays(ref arr1, ref arr2);
        }
        
        int[] cnts2 = new int[numberOfDigits];
        foreach (int num in arr2) {
            for (int j = 0; j < numberOfDigits; j++) {
                if ((num & (1 << j)) > 0) {
                    cnts2[j]++;
                }
            }
        }
        
        int result = 0;
        foreach (int num in arr1) {
            for (int j = 0; j < numberOfDigits; j++) {
                if ((num & (1 << j)) > 0) {
                    result ^= (1 << j) * (cnts2[j] % 2);
                }
            }
        }
        
        return result;
    }

    private int GetNumberOfDigits(int[] arr) {
        int maxVal = 0;
        foreach (int num in arr) {
            maxVal = Math.Max(maxVal, num);
        }
        return Convert.ToString(maxVal, 2).Length;
    }

    private void SwapArrays(ref int[] arr1, ref int[] arr2) {
        int[] temp = arr1;
        arr1 = arr2;
        arr2 = temp;
    }
}

// @lc code=end

