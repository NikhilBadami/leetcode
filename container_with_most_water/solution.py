class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        To calculate total water stored, take x-axis coordinates and subtract them to get base and then take height of
        shorter bound and calculate area of rectangle. This is total water that can be stored. Note that there can be
        bars higher than the shorter bar. Imagine the water is flowing from the top, not sideways so taller bars will
        not impeded filling the container.

        Naive solution would be to double loop every entry in height and find the max area combination. This is an O(n^2)
        solution though, is there a better way?

        A more efficient approach could be to start two pointers at the beginning and end of the array respectively,
        and then increment the pointer pointing to the shorter bar. This is because the shorter bar is limiting the
        max container size so it makes sense to search for a larger bar from that pointer instead of the taller pointer.

        time: O(n)
        memory: O(1)
        """
        l, r = 0, len(height) - 1
        max_area = -1

        while l < r:
            height_bound = min(height[l], height[r])
            bottom_bound = r - l
            max_area = max(max_area, bottom_bound * height_bound)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
