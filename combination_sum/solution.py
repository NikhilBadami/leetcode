class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        The goal is to find all combinations of the numbers in candidates that sum to target. Numbers within the candidates
        array can be used multiple times. The ending cases are:

        1. The numbers sum to targets
        2: The numbers exceed target
        3: The current index exceeds the length of candidates

        Note that each candidate list must be unique. 

        First question is how will I iterate through candidates to generate possible solutions. Another way to look at this
        is at each index within candidates, what choices can I make? The first choice is to use the number at the current
        index. The second choice is to advance the index to the next value. If I choose to use the current number, I need
        to add it to the running sum and then recurse to solve the same problem with the current sum. If I choose to
        advance the index, I increment the current index and recurse. This suggests a recursive nature to this problem.
        Within each recursion, I am looping starting from a given index, a given running sum and the target. Note that 
        because I can re-use elements, using breadth first search can lead to duplicates. Consider the example where
        the q only has 1 set. On the first iteration, I pop the queue, add the element at the current index, then add
        both sets back to the queue. On the next iteration if I haven't advanced the candidates list idx, I will regenerate
        the set I just generated in addition to the new sets, very quickly leading to lots of duplicates.

        If I am recursing, on each iteration, I want to take the following information: The current index into candidates,
        the current running sum, the candidates array, the target, and the current candidate solution. Within each
        recurse, I am either recursing into the next step of the problem, or iterating through the candidates array starting
        at the given index.

        The time complexity is determined as follows. At each index, I can make two choices: I can either use the current
        element to build the solution, or I can progress to the next element. Making a binary decision at each element has
        a time complexity of 2^n and I can do this at most n times.

        time: O(n * 2^n)
        memory: O(n * 2^n)
        """
        return self._helper(0, candidates[0], [candidates[0]], candidates, target, [])
    
    def _helper(
        self,
        cur_idx,
        cur_sum,
        cur_soln,
        candidates,
        target,
        res
    ):
        """
        Helper function to calculate solutions. Returns a list containing running list of all valid solutions
        """
        # Handle terminating cases
        if cur_idx >= len(candidates) or cur_sum > target:
            return res
        if cur_sum == target:
            res.append(cur_soln)
            return res
        
        # Include the current element into the running solution and recurse
        cur_soln.append(candidates[cur_idx])
        cur_sum += candidates[cur_idx]
        self._helper(cur_idx, cur_sum, cur_soln[:], candidates, target, res)
        # Remove current element from solution
        cur_soln.pop()
        cur_sum -= candidates[cur_idx]

        # Make second choice to iterate starting at the current index
        for i in range(cur_idx+1, len(candidates)):
            cur_soln.append(candidates[i])
            cur_sum += candidates[i]
            self._helper(i, cur_sum, cur_soln, candidates, target, res.copy())
            cur_soln.pop()
            cur_sum -= candidates[i]
        return res


