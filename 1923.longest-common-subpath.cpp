/*
 * @lc app=leetcode id=1923 lang=cpp
 *
 * [1923] Longest Common Subpath
 */

// @lc code=start
#include <vector>
#include <unordered_map>
using std::equal;
using std::unordered_map;
using std::vector;

class Solution 
{
public:
    int longestCommonSubpath(int n, vector<vector<int>>& ps) 
    {
        int l = 0;        
        int r = min_element(ps.begin(), ps.end(), [](const auto &a, const auto &b){ return a.size() < b.size(); })->size() + 1;
        long long base = 100003;
        long long mod = (long long) 1000000007;
        while (l < r) 
        {
            int m = l + (r - l) / 2;
            unordered_map<long long, vector<int>> hs;
            for (int i = 0; i < ps.size() && (i == 0 || !hs.empty()); ++i) 
            {
                long long hash = 0, d = 1;
                unordered_map<long long, vector<int>> hs1;
                for (int j = 0; j < ps[i].size(); ++j) 
                {
                    hash *= base;
                    hash %= mod;
                    hash += ps[i][j];
                    hash %= mod;
                    if (j >= m)
                    {
                        hash -= d * ps[i][j - m];
                        while (hash < 0)
                        {
                            hash += mod;
                        }                   
                    }
                    else
                    {
                        d *= base;
                        d %= mod;
                    }                          
                    if (j >= m - 1)
                    {
                        if (i == 0)
                        {
                            hs1[hash].push_back(j - (m - 1));
                        }
                        else if (hs.count(hash) != 0)
                        {
                            for (int start : hs[hash])
                            {
                                if (equal(ps[0].begin() + start, ps[0].begin() + start + m, ps[i].begin() + j - (m - 1)))
                                {
                                    hs1[hash].push_back(start);
                                    break;
                                }
                            }
                        }                   
                    }                        
                }
                swap(hs, hs1);
            }
            if (!hs.empty())
            {
                l = m + 1;
            }                
            else
            {
                r = m;
            }                            
        }
        return l - 1;
    }
};
// @lc code=end

