#
# @lc app=leetcode id=1912 lang=python3
#
# [1912] Design Movie Rental System
#

# @lc code=start
import heapq
from typing import List

from sortedcontainers import SortedList


class MovieRentingSystem:
    '''
    To satisfy the requirement, We should keep a rented and unrented data structure
    Search: unrented = Dictionary<movie, minHeap<price, shop>>
    Report: rented = SortedSet<price, shop, movie>. Lazy update unrented when Search is called
    Rent / Drop: we do not know the price. So we also need a Dictionary<<shop, movie>, price>
    '''

    def __init__(self, n: int, entries: List[List[int]]):
        self.free = {}
        self.db = {}
        self.rented = SortedList()
        for shop, movie, price in entries:
            self.db[(shop, movie)] = price
            if movie not in self.free:
                self.free[movie] = SortedList()
            self.free[movie].add([price, shop])

    def search(self, movie: int) -> List[int]:
        result = []
        if movie in self.free:
            for price, shop in self.free[movie].islice(0, min(5, len(self.free[movie]))):
                result.append(shop)
        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add([self.db[(shop, movie)], shop, movie])
        self.free[movie].remove([self.db[(shop, movie)], shop])

    def drop(self, shop: int, movie: int) -> None:
        self.rented.remove([self.db[(shop, movie)], shop, movie])
        self.free[movie].add([self.db[(shop, movie)], shop])

    def report(self) -> List[List[int]]:
        result = []
        for price, shop, movie in self.rented.islice(0, min(5, len(self.rented))):
            result.append([shop, movie])
        return result


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
# @lc code=end

