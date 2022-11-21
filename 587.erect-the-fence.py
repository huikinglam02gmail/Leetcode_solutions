#
# @lc app=leetcode id=587 lang=python3
#
# [587] Erect the Fence
#

# @lc code=start
class Solution:
    """Computes the convex hull of a set of 2D points.

    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
      starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    """  
    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(self, o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])    
    
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # Sort the points lexicographically (tuples are compared lexicographically).
        # Remove duplicates to detect the case we have just one unique point.
        trees.sort()

        # Boring case: no points or a single point, possibly repeated multiple times.
        if len(trees) == 1:
            return trees

        # Build lower hull 
        lower = []
        for p in trees:
            while len(lower) >= 2 and self.cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # Build upper hull
        upper = []
        for p in reversed(trees):
            while len(upper) >= 2 and self.cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)
            
        # Concatenation of the lower and upper hulls gives the convex hull.
        # Last point of each list is omitted because it is repeated at the beginning of the other list. 
        boundary = set()
        for item in lower:
            boundary.add(tuple(item))
        for item in upper:
            boundary.add(tuple(item))
        result = []
        for item in list(boundary):
            result.append(list(item))
        return result
# @lc code=end

