/*
 * @lc app=leetcode id=2043 lang=csharp
 *
 * [2043] Simple Bank System
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Bank {
    private long[] Balance;

    public Bank(long[] balance) {
        Balance = balance.Select(x => x).ToArray();
    }

    public bool Transfer(int account1, int account2, long money) {
        if (account1 - 1 < 0 || account1 - 1 >= Balance.Length) return false;
        if (account2 - 1 < 0 || account2 - 1 >= Balance.Length) return false;
        if (Balance[account1 - 1] < money) return false;

        Balance[account1 - 1] -= money;
        Balance[account2 - 1] += money;
        return true;
    }

    public bool Deposit(int account, long money) {
        if (account - 1 < 0 || account - 1 >= Balance.Length) return false;
        Balance[account - 1] += money;
        return true;
    }

    public bool Withdraw(int account, long money) {
        if (account - 1 < 0 || account - 1 >= Balance.Length) return false;
        if (Balance[account - 1] < money) return false;

        Balance[account - 1] -= money;
        return true;
    }
}


/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * bool param_1 = obj.Transfer(account1,account2,money);
 * bool param_2 = obj.Deposit(account,money);
 * bool param_3 = obj.Withdraw(account,money);
 */
// @lc code=end

