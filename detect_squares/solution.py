"""
I need to design a class that can take and store a stream of coordinates for points on an x-y plane. The class should also be able to take a
query point and count the number of ways to take 3 additional points that exist in the data structure and form an axis aligned square. The
coordinates will always be positive, so the square can only exist in the first quadrant of the graph plane.

A square can be defined by two points that form a diagonal line, so given a query point, I can first check to see if a diagonal point exists
in the data structure. How can I check for diagonal points? Diagonal points are defined from the query point as (x +/- n, y +/- n). I know that
the points are bounded in the range [0, 1000]. One way to do this would be, starting from the query point, start a search in both directions
witin the bounds of the problem and search for possible diagonal points. If they exist, move on to the next step.

If I find a valid diagonal point, the next step is to find the other two points. This should be straight forward given these two points. Say I
have the points (4,4) and (2,2) as my diagonal points. I know that the other points must be (2, 4) and (4, 2). I can directly check if these
points exist in the array. If they do, I can add this to the count of ways I can create a square. I continue until I've counted all possible ways
to create a square.

The search for a diagonal can be inefficient if I naively check within the bounds (0, 1000). How can I make this more efficient? I can keep track
of a max x and y value for any point in the data structure and use this as my bounds for the search. For example, if I know the max X coordinate
for any point in the structure is 5, the point (6,6) cannot exist in the data structure so there is no point searching beyond 5. Similarly, if
the max y value for and point is 2, the point (3, 3) cannot exist. I can keep track of and update the max x and y value in the data structure
on each add operation.

How do I store the points? I need to be able to efficiently look up points that exist within the data structure. I can accomplish this using a
hash map that hashes each coordinate as a tuple.

Finally, how do I handle duplicate points? I hash each coordinate pair to the count of times it occurrs in the datastructure. If I find a square
that uses a point that has multiple occurrences, I look at the point with the lowest number of occurrences and add that to my count of squares.
For example, if I have a square defined by (3,3), (2,2), (2,3) and (3,2) and point (3,2) has the lowest count of 2, then I can only create 2
squares from this set of points.

The time complexity of the add operation is O(1) since I am storing it in a hashmap. The memory complexity is O(n) where n is the number of points
that are added to the structure.

The time complexity of the count operation is O(min(x, y)) where x, y represent the max x value and max y value respectively that are stored in the
structure. The search will stop at the lower of these two bounds. Looking up companion points once a diagonal point is found is an O(1) operation
since the points are stored in a hash map.
"""

class DetectSquares:

    def __init__(self):
        """
        This class initializes a hashmap to store points as well as a max x and y value, set to -1 initially
        """
        self.points = {}
        self.max_x = -1
        self.max_y = -1
        self.min_x = 1001
        self.min_y = 1001

    def add(self, point: List[int]) -> None:
        """
        Adds a point to the data structure and updates the max x and y values if appropriate

        time: O(1)
        memory: O(n) --> n is the number of points the structure stores. Note that n memory is not used in this operation directly, but it is
                         referenced since we are adding to the total number of points the structure stores
        """
        # Store point
        tup_point = tuple(point)
        self.points[tup_point] = self.points.get(tup_point, 0) + 1
        # Update max x and y if applicable
        self.max_x = max(self.max_x, tup_point[0])
        self.max_y = max(self.max_y, tup_point[1])
        # Update min x and y if applicable
        self.min_x = min(self.min_x, tup_point[0])
        self.min_y = min(self.min_y, tup_point[1])

    def count(self, point: List[int]) -> int:
        """
        Search for all sets of points that form an axis aligned square.

        time: O(min(max_x, max_y))
        memory: O(1)
        """
        num_ways = 0
        # Check if at least 3 distinct points exist in the structure
        if len(self.points.keys()) < 3:
            return num_ways
        
        # Search for a diagonal point
        # First search towards min(max_x, max_y)
        tup_point = tuple(point)
        for i in range(1, min(self.max_x, self.max_y)):
            if (point[0] + i, point[1] + i) in self.points.keys():
                # See if the companion points exist
                diag_x = point[0] + i
                diag_y = point[1] + i
                # Check if point below diag point exists
                if (diag_x, point[1]) in self.points.keys():
                    # Only if this point exists, then I will chcek if the point above the query point exists
                    # Find the min count of all the points
                    pt1_count = self.points(tup_point)
                    pt2_count = self.point((diag_x, diag_y))
                    pt3_count = self.point((diag_x, point[1]))
                    pt4_count = self.point((point[0], diag_y))
                    min_count = min(
                        pt1_count,
                        pt2_count,
                        pt3_count,
                        pt4_count
                    )
                    num_ways += min_count
        # Perform similar search towards smallest point
        for i in range(1, max(self.min_x, self.min_y)):
            if (point[0] - i, point[1] - i) in self.points.keys():
                 # See if the companion points exist
                diag_x = point[0] - i
                diag_y = point[1] - i
                # Check if point below diag point exists
                if (diag_x, point[1]) in self.points.keys():
                    # Only if this point exists, then I will chcek if the point above the query point exists
                    # Find the min count of all the points
                    pt1_count = self.points(tup_point)
                    pt2_count = self.point((diag_x, diag_y))
                    pt3_count = self.point((diag_x, point[1]))
                    pt4_count = self.point((point[0], diag_y))
                    min_count = min(
                        pt1_count,
                        pt2_count,
                        pt3_count,
                        pt4_count
                    )
                    num_ways += min_count
        return num_ways


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
