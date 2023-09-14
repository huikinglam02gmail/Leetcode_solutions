/*
 * @lc app=leetcode id=332 lang=csharp
 *
 * [332] Reconstruct Itinerary
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    private Dictionary<string, List<(int, string)>> graph;
    private bool found;
    private string result;
    private bool[] used;

    public IList<string> FindItinerary(IList<IList<string>> tickets) {
        graph = new Dictionary<string, List<(int, string)>>();
        found = false;
        result = "";
        used = new bool[tickets.Count];

        tickets = tickets.OrderBy(ticket => ticket[1]).ToList();

        for (int i = 0; i < tickets.Count; i++) {
            string from = tickets[i][0];
            string to = tickets[i][1];
            if (!graph.ContainsKey(from)) {
                graph[from] = new List<(int, string)>();
            }
            graph[from].Add((i, to));
        }

        DFS("JFK", "");

        List<string> stringList = new List<string>();
        int j = 0;
        while (j < result.Length) {
            stringList.Add(result.Substring(j, 3));
            j += 3;
        }

        return stringList;
    }

    private void DFS(string current, string itinerary) {
        if (used.All(val => val == true)) {
            result = itinerary + current;
            found = true;
        }
        else if (graph.ContainsKey(current) && !found) {
            foreach ((int id, string nxt) in graph[current]) {
                if (!used[id] && !found) {
                    used[id] = true;
                    DFS(nxt, itinerary + current);
                    used[id] = false;
                }
            }
        }
    }
}

// @lc code=end

