class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        I'm given an input array nums that may contain duplicates. I need to return all possible subsets of the array without returning duplicates.
        The solution can be returned in any order.

        Because I'm not required to maintain the order of the array, I can sort the input initially. This helps in identifying duplicate entries.
        Then, I can perform a breadth first search over the decision tree that forms. The tree is formed as follows:

        At each stage, I choose to include the current element, or move on to the next unique element. In other words, I don't just move to the
        next index, I move to the next index such that it does not equal whatever element is at the current index. If the current index is beyond
        the bound of the array, I do not modify this element and add it to the result.

        To track which index each element should look at, I pass each element as a tuple of (cur_soln, idx).

        time: O(2^n)
        memory: O(2^n)
        """
        # Sort input initially
        nums.sort()

        # Process sorted input
        from collections import deque
        q = deque()
        res = []
        q.append(([], 0))
        while len(q) != 0:
            # Get current element
            cur_soln, idx = q.popleft()
            # First check if this solution is "complete"
            if idx >= len(nums):
                res.append(cur_soln)
                continue
            # Create two entries. One uses the current solution, but advances the index to the next unique element, or the end of the list if
            # non exist. The next uses the current index
            # Use current index
            new_soln = cur_soln.copy()
            new_soln.append(nums[idx])
            # Advance the index by 1
            idx += 1
            q.append((new_soln, idx))

            # Re-use the same solution but advance the index to the next unique element
            if idx < len(nums):
                while idx < len(nums) and nums[idx] == nums[idx - 1]:
                    idx += 1
            q.append((cur_soln, idx))
        return res

