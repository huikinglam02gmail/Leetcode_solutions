/*
 * @lc app=leetcode id=2801 lang=cpp
 *
 * [2801] Count Stepping Numbers in Range
 */

// @lc code=start
#include <map>
#include <tuple>
#include <string>

class Solution {
private:
    const long long MOD = 1000000007;
    std::map<std::tuple<int, bool, int, std::string>, long> cache;

public:
    int countSteppingNumbers(std::string low, std::string high) {
        cache.clear();
        return static_cast<int>((Count(high) - Count(MinusOne(low)) + MOD) % MOD);
    }

private:
    long long DP(int i, bool tight, int lastDigit, const std::string& num) {
        auto t = std::make_tuple(i, tight, lastDigit, num);
        
        if (i == num.length()) {
            return 1;
        }
        
        if (cache.find(t) == cache.end()) {
            int maxDigit = tight ? num[i] - '0' : 9;
            long ans = 0;
            
            for (int d = 0; d <= maxDigit; d++) {
                bool nxtTight = tight && d == maxDigit;
                
                if (lastDigit == -1) {
                    int d1 = (d == 0) ? -1 : d;
                    ans += DP(i + 1, nxtTight, d1, num);
                    ans %= MOD;
                }
                else if (std::abs(lastDigit - d) == 1) {
                    ans += DP(i + 1, nxtTight, d, num);
                    ans %= MOD;
                }
            }
            cache[t] = ans;
        }
        
        return cache[t];
    }
    
    long long Count(const std::string& num) {
        return DP(0, true, -1, num);
    }
    
    std::string MinusOne(const std::string& s) {
        std::string str = s;
        int carry = 1;
        for (int i = str.length() - 1; i >= 0; i--) {
            str[i] -= carry;
            carry = 0;
            if (str[i] < '0') {
                str[i] += 10;
                carry++;
            }
        }
        int idx = 0;
        while (idx < str.length() && str[idx] == '0') {
            idx++;
        }
        return str.substr(idx);
    }
};
// @lc code=end

