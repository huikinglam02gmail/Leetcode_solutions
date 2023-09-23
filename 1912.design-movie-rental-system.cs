/*
 * @lc app=leetcode id=1912 lang=csharp
 *
 * [1912] Design Movie Rental System
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class MovieRentingSystem {
    private readonly Dictionary<int, SortedSet<(int, int)>> unrented;
    private readonly Dictionary<(int, int), int> rented;
    private readonly SortedSet<(int, int, int)> rentedSorted;

    public MovieRentingSystem(int n, int[][] entries) {
        unrented = new Dictionary<int, SortedSet<(int, int)>>();
        rented = new Dictionary<(int, int), int>();
        rentedSorted = new SortedSet<(int, int, int)>();

        foreach (var entry in entries) {
            int shop = entry[0];
            int movie = entry[1];
            int price = entry[2];

            if (!unrented.ContainsKey(movie)) {
                unrented[movie] = new SortedSet<(int, int)>();
            }

            unrented[movie].Add((price, shop));
            rented[(shop, movie)] = price;
        }
    }

    public IList<int> Search(int movie) {
        List<int> result = new List<int>();
        if (unrented.ContainsKey(movie)) {
            foreach ((int price, int shop) in unrented[movie].Take(5)) {
                result.Add(shop);
            }
        }
        return result;
    }

    public void Rent(int shop, int movie) {
        int price = rented[(shop, movie)];
        rentedSorted.Add((price, shop, movie));
        unrented[movie].Remove((price, shop));
    }

    public void Drop(int shop, int movie) {
        int price = rented[(shop, movie)];
        rentedSorted.Remove((price, shop, movie));
        unrented[movie].Add((price, shop));
    }

    public IList<IList<int>> Report() {
        List<IList<int>> result = new List<IList<int>>();
        foreach ((int price, int shop, int movie) in rentedSorted.Take(5)) {
            result.Add(new List<int> { shop, movie });
        }
        return result;
    }
}


/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem obj = new MovieRentingSystem(n, entries);
 * IList<int> param_1 = obj.Search(movie);
 * obj.Rent(shop,movie);
 * obj.Drop(shop,movie);
 * IList<IList<int>> param_4 = obj.Report();
 */
// @lc code=end

