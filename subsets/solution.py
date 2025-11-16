class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        A subset is a selection of array elements that may not be continguous and may be empty. When creating all subsets,
        one possible approach is to view the creation as a tree. At each element in the tree, I have the option to either
        include the current element in the subset, or to not include it. This will naturally create a tree where each
        of these choices creates divergent paths. I can iterate through this tree using breadth first search

        time: For each element, I can make two branching choices so 2^n time
              O(2^n)
        memory: O(2^n) since I need to store each subset
        """
        from collections import deque
        q = deque()
        # Start with the empty set
        q.append([])
        # index for nums list
        i = 0
        while i < len(nums):
            # For each given nums element, I need to pop each possible subset I've seen so far and make the decision
            # to either add the current element to it or not. I can store these elements in a temporary q
            temp_q = deque()
            while len(q):
                subset = q.popleft()
                # add current element to subset
                new_subset = subset.copy()
                new_subset.append(nums[i])
                # Store both new and old subset in temp q
                temp_q.append(subset)
                temp_q.append(new_subset)
            # Add all elements back into the queue
            while len(temp_q):
                q.append(temp_q.popleft())
            
            # Move to the next element of nums
            i += 1
        return list(q)
        
