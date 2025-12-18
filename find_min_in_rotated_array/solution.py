class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Goal is to find the minimum value in an array that is sorted in ascending order and has been rotated n times. All
        the numbers in the array are unique. Because of the sorting method and because all the numbers are unique, the
        minimum value is the value such that it is both less than the value immediately before it and after it.

        I can use binary search to find this value quickly. Basically, use the standard binary search algorithm with some
        changes. If the mid point is both larger than the left and right bounds, I am in a rotated part of the array
        and the minimum exists to the right of this value. If the mid point is less than the right bound but greater than
        the left bound, then I am in a section of the array that contains the minimum.

        time: O(log(n))
        memory: O(1)
        """
        # Edge case array has 1 element
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            mid_pt = l + (r-l) // 2
            right_el = mid_pt + 1 if mid_pt != len(nums) - 1 else 0
            if nums[mid_pt] < nums[mid_pt-1] and nums[mid_pt] < nums[right_el]:
                return nums[mid_pt]
            elif nums[mid_pt] >= nums[l] and nums[mid_pt] >= nums[r]:
                l = mid_pt + 1
            else:
                r = mid_pt - 1
        return None

