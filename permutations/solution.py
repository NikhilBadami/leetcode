class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given an input array, I need to create all permutations of the array. A permutation is a rearranement of the value in the
        array. I can accomplish this as follows:

        I start with an empty set. Additionally, I track which elements are available for me to use. With the empty set, all elements
        are available for me to use. I iterate through the array and add each element individually to the empty set, creating a
        recursive call. On each recursive call, I iterate through the array again, however this time, I cannot use the element I
        used in the empty set. For example, if I have an input of [1,2,3], the first recursive call would create an array with a
        value [1]. On this recursive call, I cannot re-use 1, I can only add 2 or 3. To enforce this, I will also pass along a set
        that tracks which indices are available to use at each level of the recursion tree.

        time: O(n!)
        memory: O(n)
        """
        return self._helper(nums, [], set())
    
    def _helper(self, nums, cur_soln, unavailable_idx):
        """
        Helper function takes input nums, the current running solutions and the available indices
        """
        if len(cur_soln) == len(nums):
            # This is a finished permutation
            return [cur_soln.copy()]
        
        # Loop through nums. If the index is available, append it to the current solution and make a recursive call
        res = None
        for i in range(len(nums)):
            if i not in unavailable_idx:
                cur_soln.append(nums[i])
                unavailable_idx.add(i)
                soln = self._helper(nums, cur_soln, unavailable_idx)
                if res:
                    res += soln
                else:
                    res = soln
                cur_soln.pop()
                unavailable_idx.remove(i)
        return res
        
