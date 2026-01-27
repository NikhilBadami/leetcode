class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        I'm given an array of triplets where triplets[i] = [a, b, c] and a target triplet. I need to see if I can form the target within the
        input triplets array by performing the following operation: I take two indices i, j s.t. i != j and replace triplets[j] with
        [max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)]. I can perform this operation any number of times. If triplets[j] == target at some point,
        return True. If it is not possible, return False.

        Since the problem is asking to see if it is possible to form the triplet, I do not need to actually simulate each update step, only
        check that it is not impossible to form the triplets. There are two checks I can do. first, I need to remove any triplets from the input
        that have values greater than any of the values in the target. For example, if I am looking for a target = [2,7,5] and the input has a
        triplet [1,8,5], I do not want to ever consider this triplet since if I perform the merge operation, which takes a max of the elements
        in the two triplets being compared, I will always end up with 8. Any subsequent merges after this will always have 8 or higher, so I
        want to remove any triplets where this could occurr. Additionally, I want to ensure that the value in the target actually exists at
        the index. For example, if I have a target [3,2,1] but there is no 3 at the first index of any triplet, then it is not possible to form
        the target. If the above conditions are both false, then it is possible to form the solution.

        I can do this in two steps. First, filter the input array and remove any triplets that have values greater than any of the target values.
        Second, process the triplet array into sets, one for each index, and check to see if the target values exist in these sets. If they
        don't, it is not possible to form the solution.

        time: O(n)
        memory: O(n)
        """
        # Filter out triplets that have values larger than any of the target indices
        filtered = [t for t in triplets if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]]
        if len(filtered) == 0:
            return False
        
        # Process remaining triplets into sets, one for each index
        idx_1 = set()
        idx_2 = set()
        idx_3 = set()
        for t in filtered:
            idx_1.add(t[0])
            idx_2.add(t[1])
            idx_3.add(t[2])
        
        # Check to see if all target values exist at the right indices in triplets
        if target[0] not in idx_1 or target[1] not in idx_2 or target[2] not in idx_3:
            return False
        return True
        
