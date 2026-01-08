class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        I'm given an array of unique numbers that are sorted in ascending order and possibly rotated some number of times. I need to
        find the given target in this array and return its index or return -1 if the target does not exist in the array.

        To solve this, I can first find the minimum value of the array. I can find this value as follows

        Using a binary search which I initialize normally (i.e., l = 0, r = len(nums) - 1) I can find the min element in O(log(n)) time
        using the following conditions:

        1: If the mid point element is less than both of its neighbors, it must be the smallest element. This is true because the
           array is sorted in ascending order and there are no duplicates, to there will only be one element that satisfies this
           condition
        2: If the mid point is greater than both bounds of the array, I am in a rotated part of the array that cannot contain the min
           and I have to search to the left of this element
        3: If the above two conditions are not true, I search to the left of this element (i.e, I'm in a part of the array that
           contains the minimum)
        
        Once I have the minimum element, I can partition the array based on where the target might be. For example, I can check
        if the target is within the bounds of the rotated array i.e., b1 <= target <= b2 and search only that part of the array
        or I can check the part of the array that has the minimum in it.

        time: O(log(n))
        memory: O(1)
        """
        # The min finding algorithm breaks if there is only 1 element in the array, so this is handled separately
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        # Find the minimum value in the array
        l, r = 0, len(nums) - 1
        min_idx = -1
        while l <= r:
            mid = l + (r - l) // 2
            # Set a right element in case the mid point is the last index of the array
            right = mid + 1 if mid + 1 < len(nums) else 0
            if nums[mid] < nums[mid-1] and nums[mid] < nums[right]:
                min_idx = mid
                break
            elif nums[mid] >= nums[0] and nums[mid] >= nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        
        # Now that i have the minimum index, I can partition the array and check which side I should search for the target
        # Check if the target could be in the rotated part of the array (i.e., to the left of the minimum)
        l, r = -1, -1
        if target >= nums[0] and target <= nums[min_idx-1]:
            # Search this part of the array for the target
            l = 0
            r = min_idx - 1 if min_idx - 1 >= 0 else len(nums) - 1
        else:
            # Search non-rotated part of the array
            l, r = min_idx, len(nums) - 1

        while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
