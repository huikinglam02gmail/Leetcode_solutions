/*
 * @lc app=leetcode id=2614 lang=cpp
 *
 * [2614] Prime In Diagonal
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /*
    Get all the diagonal elements, sort from high to low
    Sieve of Eratosthenes to get all the primes below or equal to max(diagonal)
    Report the number if it is inside the prime list
    */
    int diagonalPrime(std::vector<std::vector<int>>& nums) {
        std::vector<int> diagonals;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            diagonals.push_back(nums[i][i]);
            diagonals.push_back(nums[i][n - 1 - i]);
        }

        std::sort(diagonals.rbegin(), diagonals.rend());

        std::vector<int> allPrimes = smallestPrimeSieveOfEratosthenes(diagonals[0]);

        for (int d : diagonals) {
            if (d > 1 && allPrimes[d] == d) {
                return d;
            }
        }

        return 0;
    }

    /*
    C++ program to return the smallest prime divisor smaller than or equal to n using Sieve of Eratosthenes 
    */
    std::vector<int> smallestPrimeSieveOfEratosthenes(int n) {
        std::vector<int> prime(n + 1);

        for (int i = 0; i <= n; i++) {
            prime[i] = i;
        }

        int p = 2;

        while (p * p <= n) {
            if (prime[p] == p) {
                for (int i = p * p; i <= n; i += p) {
                    if (prime[i] == i) {
                        prime[i] = p;
                    }
                }
            }

            p++;
        }

        return prime;
    }
};

// @lc code=end

