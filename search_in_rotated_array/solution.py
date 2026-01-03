class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        I'm given an array of unique elements that is sorted in ascending order and is possibly rotated. I need to search this array
        for the given target. I know how to find the minimum in a rotated array. The element that is less than both the preceeding
        element and the one after it must be the minimum element.

        To find an arbitrary target, I can first find the minimum of the array. This tells me how much the array has been rotated.
        Then, I conduct a binary search while and once the mid point has been found, I offset the left, right and mid point bounds
        to check where in the array I should continue searching for the target.

        time: O(log(n))
        memory: O(1)
        """
        # Check edge case
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        # First, find the minimum of the array
        l, r = 0, len(nums) - 1
        min_idx = -1
        while l <= r:
            mid_pt = l + (r-l) // 2
            right_el = mid_pt + 1 if mid_pt != len(nums) - 1 else 0
            if nums[mid_pt] < nums[mid_pt-1] and nums[mid_pt] < nums[right_el]:
                min_idx = mid_pt
                break
            elif nums[mid_pt] >= nums[l] and nums[mid_pt] >= nums[r]:
                l = mid_pt + 1
            else:
                r = mid_pt - 1
       
        # Search for the target using the min index as an offset
        l, r = 0, len(nums) - 1
        offset = len(nums) - min_idx
        while l <= r:
            mid_pt = l + (r - l) // 2
            # Offset all pointers
            mid_pt_offset = mid_pt - offset
            l_offset = l - offset
            r_offset = r - offset
            if nums[mid_pt_offset] == target:
                return mid_pt_offset + len(nums) if mid_pt_offset < 0 else mid_pt_offset
            # Update the bounds based before the offset
            if nums[mid_pt_offset] > target:
                r = mid_pt - 1
            else:
                l = mid_pt + 1
        return -1

