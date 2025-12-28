class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        This problem is similar to the subsets problem where I cannot use numbers more than once. This means the branching
        factor is the same as the subsets problem: either I use the current element or I don't and then proceed to the
        next index. The caveat with this problem is I only return solutions that sum to target. This means that instead
        of the queue just storing the existing subsets, they must store tuples that contain both the existing subset so
        far as well as the running sum of that subset. Additionally, because I have a target who's solution I am looking for
        I can get a small efficiency increase by pre-sorting the array so that I can stop early if I encounter any value
        greater than the target, preventing unnecessary tree exploration

        time: O(2^n) --> Technically there is an O(nlog(n)) pre-processing time but this is dwarfed by the overall run
        time complexity of the algorithm
        memory: O(2^n) worst case
        """
        # Pre-sort array
        candidates.sort()

        from collections import deque
        q = deque()
        
        i = 0
        q.append(([], 0))
        while i < len(candidates):
            if candidates[i] > target:
                # No possible solutions exist beyond this point
                break

            cur_sets = len(q)
            for _ in range(cur_sets):
                # Pop off existing solutions from the queue. For each one, create a copy and then append the current
                # index to the copy while keeping the original
                s = q.popleft()
                cur_soln, cur_sum = s
                new_soln = cur_soln.copy()
                new_soln.append(candidates[i])
                new_sum = cur_sum + candidates[i]
                q.append((cur_soln, cur_sum))
                # Only add the new solution if its sum <= target
                if new_sum <= target:
                    q.append((new_soln, new_sum))

            # Each number can only be used once, so if the next value equals the current value, it should be skipped
            i += 1
    
        # post-process q to get solutions that equal target
        res = []
        while len(q):
            soln, _sum = q.popleft()
            if _sum == target:
                res.append(tuple(soln))
        return list(set(res))
        
