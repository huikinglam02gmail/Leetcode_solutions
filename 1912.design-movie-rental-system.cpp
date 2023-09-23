/*
 * @lc app=leetcode id=1912 lang=cpp
 *
 * [1912] Design Movie Rental System
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

class MovieRentingSystem {
private:
    unordered_map<int, set<pair<int, int>>> unrented;
    map<pair<int, int>, int> rented;
    set<tuple<int, int, int>> rentedSorted;

public:
    MovieRentingSystem(int n, vector<vector<int>>& entries) {
        for (const auto& entry : entries) {
            int shop = entry[0];
            int movie = entry[1];
            int price = entry[2];

            if (unrented.find(movie) == unrented.end()) {
                unrented[movie] = set<pair<int, int>>();
            }

            unrented[movie].insert({price, shop});
            rented[{shop, movie}] = price;
        }
    }

    vector<int> search(int movie) {
        vector<int> result;
        if (unrented.find(movie) != unrented.end()) {
            auto it = unrented[movie].begin();
            int count = 0;
            while (count < 5 && it != unrented[movie].end()) {
                result.push_back(it->second);
                ++it;
                ++count;
            }
        }
        return result;
    }

    void rent(int shop, int movie) {
        int price = rented[{shop, movie}];
        rentedSorted.insert({price, shop, movie});
        unrented[movie].erase({price, shop});
    }

    void drop(int shop, int movie) {
        int price = rented[{shop, movie}];
        rentedSorted.erase({price, shop, movie});
        unrented[movie].insert({price, shop});
    }

    vector<vector<int>> report() {
        vector<vector<int>> result;
        auto it = rentedSorted.begin();
        int count = 0;
        while (count < 5 && it != rentedSorted.end()) {
            result.push_back({get<1>(*it), get<2>(*it)});
            ++it;
            ++count;
        }
        return result;
    }
};


/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem* obj = new MovieRentingSystem(n, entries);
 * vector<int> param_1 = obj->search(movie);
 * obj->rent(shop,movie);
 * obj->drop(shop,movie);
 * vector<vector<int>> param_4 = obj->report();
 */
// @lc code=end

