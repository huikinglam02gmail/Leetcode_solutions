/*
 * @lc app=leetcode id=341 lang=csharp
 *
 * [341] Flatten Nested List Iterator
 */

// @lc code=start
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool IsInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     int GetInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     IList<NestedInteger> GetList();
 * }
 */
using System.Collections.Generic;

public class NestedIterator {
    private readonly Stack<(IList<NestedInteger>, int)> stack;

    public NestedIterator(IList<NestedInteger> nestedList) {
        stack = new Stack<(IList<NestedInteger>, int)>();
        stack.Push((nestedList, 0));
    }

    public int Next() {
        var (nestedList, index) = stack.Peek();
        var result = nestedList[index].GetInteger();
        var topElement = stack.Pop();
        topElement.Item2++;
        stack.Push(topElement);
        return result;
    }

    public bool HasNext() {
        while (stack.Count > 0) {
            var (nestedList, index) = stack.Peek();

            if (index == nestedList.Count) {
                stack.Pop();
            } else if (nestedList[index].IsInteger()) {
                return true;
            } else {
                var topElement = stack.Pop();
                topElement.Item2++;
                stack.Push(topElement);
                stack.Push((nestedList[index].GetList(), 0));
            }
        }

        return false;
    }
}


/**
 * Your NestedIterator will be called like this:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.HasNext()) v[f()] = i.Next();
 */
// @lc code=end

