/*
 * @lc app=leetcode id=2272 lang=cpp
 *
 * [2272] Substring With Largest Variance
 */

// @lc code=start
#include<string>
#include<vector>
#include<algorithm>
#include<functional>
using std::max;
using std::negate;
using std::string;
using std::transform;
using std::vector;
class Solution {
private:
    int Kadane(vector<int> & arr) {
        int current = 0;
        int result = 0;
        bool beginMinus = false;
        bool hasMinus = false;
        
        for (int num : arr) {
            if (num == -1) {
                hasMinus = true;
                if (current >= 0 && beginMinus) {
                    beginMinus = false;
                    current += 1;
                }
            }
            
            current += num;
            
            if (current < 0) {
                current = -1;
                beginMinus = true;
            }
            else if (hasMinus) {
                result = max(result, current);
            }
        }
        
        return result;
    }
public:
    int largestVariance(string s) {
        int result = 0;
        vector<vector<int>> occur = vector<vector<int>>(26, vector<int> {});


        for (int i = 0; i < s.size(); i++) {
            occur[s[i] - 'a'].push_back(i);
        }

        for (int i = 0; i < 25; i++) {
            for (int j = i + 1; j < 26; j++) {
                if (occur[i].size() > 0 && occur[j].size() > 0) {
                    vector<int> subArray {};
                    int pi = 0;
                    int pj = 0;

                    // Two pointers merge
                    while (pi < occur[i].size() && pj < occur[j].size()) {
                        if (occur[i][pi] < occur[j][pj]) {
                            subArray.push_back(1);
                            pi += 1;
                        }
                        else {
                            subArray.push_back(-1);
                            pj += 1;
                        }
                    }
                    
                    while (pi < occur[i].size()) {
                        subArray.push_back(1);
                        pi += 1;
                    }
                    
                    while (pj < occur[j].size()) {
                        subArray.push_back(-1);
                        pj += 1;
                    }
                    
                    result = max(result, Kadane(subArray));
                    transform(subArray.cbegin(), subArray.cend(), subArray.begin(), negate<int>());
                    result = max(result, Kadane(subArray));
                }
            }
        }
        
        return result;
    }
};
// @lc code=end

