/*
 * @lc app=leetcode id=1993 lang=csharp
 *
 * [1993] Operations on Tree
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class LockingTree
{
    private int[] parent;
    private List<int>[] children;
    private List<Tuple<bool, int>> status;

    public LockingTree(int[] parent)
    {
        int n = parent.Length;
        this.parent = parent;
        this.status = new List<Tuple<bool, int>>(n);
        this.children = new List<int>[n];
        for (int i = 0; i < n; i++)
        {
            this.status.Add(new Tuple<bool, int>(false, -1));
            this.children[i] = new List<int>();
        }

        for (int i = 0; i < n; i++)
        {
            if (parent[i] >= 0)
            {
                this.children[parent[i]].Add(i);
            }
        }
    }

    public bool Lock(int num, int user)
    {
        if (status[num].Item1)
        {
            return false;
        }

        status[num] = new Tuple<bool, int>(true, user);
        return true;
    }

    public bool Unlock(int num, int user)
    {
        if (status[num].Item1 && status[num].Item2 == user)
        {
            status[num] = new Tuple<bool, int>(false, -1);
            return true;
        }

        return false;
    }

    private bool HasLockedAncestors(int node)
    {
        if (node == -1)
        {
            return false;
        }
        else if (status[node].Item1)
        {
            return true;
        }
        else
        {
            return HasLockedAncestors(parent[node]);
        }
    }

    private bool HasLockedDescendants(int node)
    {
        if (status[node].Item1)
        {
            return true;
        }

        foreach (var child in children[node])
        {
            if (HasLockedDescendants(child))
            {
                return true;
            }
        }

        return false;
    }

    private void UnlockDescendants(int node)
    {
        status[node] = new Tuple<bool, int>(false, -1);

        foreach (var child in children[node])
        {
            UnlockDescendants(child);
        }
    }

    public bool Upgrade(int num, int user)
    {
        if (HasLockedAncestors(num) || !HasLockedDescendants(num))
        {
            return false;
        }

        UnlockDescendants(num);
        Lock(num, user);
        return true;
    }
}


/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree obj = new LockingTree(parent);
 * bool param_1 = obj.Lock(num,user);
 * bool param_2 = obj.Unlock(num,user);
 * bool param_3 = obj.Upgrade(num,user);
 */
// @lc code=end

