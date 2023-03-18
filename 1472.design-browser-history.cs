/*
 * @lc app=leetcode id=1472 lang=csharp
 *
 * [1472] Design Browser History
 */

// @lc code=start
using System.Collections.Generic;
public class BrowserHistory 
{
    LinkedList<string> list;
    LinkedListNode<string> cursor;
    public BrowserHistory(string homepage) 
    {
        list = new LinkedList<string>(new string[1] {homepage});
        cursor = list.First;
    }
    
    public void Visit(string url) 
    {
        while (list.Last != cursor)
        {
            list.RemoveLast();
        }
        list.AddAfter(cursor, url);
        cursor = cursor.Next;
    }
    
    public string Back(int steps) 
    {
        while (steps > 0 && cursor.Previous != null)
        {
            cursor = cursor.Previous;
            steps--;
        }
        return cursor.Value;
    }
    
    public string Forward(int steps) 
    {
        while (steps > 0 && cursor.Next != null)
        {
            cursor = cursor.Next;
            steps--;
        }
        return cursor.Value;
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.Visit(url);
 * string param_2 = obj.Back(steps);
 * string param_3 = obj.Forward(steps);
 */
// @lc code=end

