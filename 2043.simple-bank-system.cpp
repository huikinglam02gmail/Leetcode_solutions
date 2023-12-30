/*
 * @lc app=leetcode id=2043 lang=cpp
 *
 * [2043] Simple Bank System
 */

// @lc code=start
#include <vector>

class Bank {
private:
    std::vector<long long> Balance;

public:
    Bank(std::vector<long long>& balance) {
        Balance.assign(balance.begin(), balance.end());
    }

    bool transfer(int account1, int account2, long long money) {
        if (account1 - 1 < 0 || account1 - 1 >= Balance.size()) return false;
        if (account2 - 1 < 0 || account2 - 1 >= Balance.size()) return false;
        if (Balance[account1 - 1] < money) return false;

        Balance[account1 - 1] -= money;
        Balance[account2 - 1] += money;
        return true;
    }

    bool deposit(int account, long long money) {
        if (account - 1 < 0 || account - 1 >= Balance.size()) return false;
        Balance[account - 1] += money;
        return true;
    }

    bool withdraw(int account, long long money) {
        if (account - 1 < 0 || account - 1 >= Balance.size()) return false;
        if (Balance[account - 1] < money) return false;

        Balance[account - 1] -= money;
        return true;
    }
};


/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */
// @lc code=end

