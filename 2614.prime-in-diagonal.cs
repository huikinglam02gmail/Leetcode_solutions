/*
 * @lc app=leetcode id=2614 lang=csharp
 *
 * [2614] Prime In Diagonal
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
    Get all the diagonal elements, sort from high to low
    Sieve of Eratosthenes to get all the primes below or equal to max(diagonal)
    Report the number if it is inside the prime list
    */
    public int DiagonalPrime(int[][] nums)
    {
        List<int> diagonals = new List<int>();
        int n = nums.Length;

        for (int i = 0; i < n; i++)
        {
            diagonals.Add(nums[i][i]);
            diagonals.Add(nums[i][n - 1 - i]);
        }

        diagonals.Sort((a, b) => b.CompareTo(a));

        int[] allPrimes = SmallestPrimeSieveOfEratosthenes(diagonals[0]);

        foreach (int d in diagonals)
        {
            if (d > 1 && allPrimes[d] == d)
            {
                return d;
            }
        }

        return 0;
    }

    /*
    C# program to return the smallest prime divisor smaller than or equal to n using Sieve of Eratosthenes 
    */
    private int[] SmallestPrimeSieveOfEratosthenes(int n)
    {
        int[] prime = new int[n + 1];
        for (int i = 0; i <= n; i++)
        {
            prime[i] = i;
        }

        int p = 2;

        while (p * p <= n)
        {
            if (prime[p] == p)
            {
                for (int i = p * p; i <= n; i += p)
                {
                    if (prime[i] == i)
                    {
                        prime[i] = p;
                    }
                }
            }

            p++;
        }

        return prime;
    }
}

// @lc code=end

