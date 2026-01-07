class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        I'm given a list of unsorted integers and need to find the longest consecutive sequence of numbers. I am not allowed to sort
        the input array as the algorithm needs to run in O(n) time.

        I can note a couple of things about this problem. First, the longest possible sequence that can be created is the length of
        the input array itself. Second, I need to be able to identify the start of a sequence. Since I am only working with the
        input array, the start of a sequence is a number whose value num-1 does not exist in the array. This is a good way to
        identify starts because the sequence has to be consecutive, so if num-1 does not exist, any preceeding sequence breaks
        at this point and a new sequence would be started.

        To find the starts of sequences efficiently, I can process the input into a set. This way, as I iterate through the array,
        I just check if num-1 is in the set. If it is, I know that this number cannot be the start of a sequence. If I find a
        sequence start, I begin iterating from this number until this sequence either breaks or is as long as the input array itself.
        Because I only iterate starting at sequence starts, I only process each number at most twice, leading to an O(n) solution.

        time: O(n)
        memory: O(n)
        """
        s = set()
        longest = 0
        # Process nums into a set
        for n in nums:
            s.add(n)
        
        # Iterate through nums again, this time to find sequence starts. Use the set instead of the input array
        # this is because duplicates do no matter for the solution. For example, if 0 is the start of a sequence,
        # it does not matter if there are multiple 0s as only one will ever be used 
        for n in s:
            if n-1 not in s:
                # This is the start of a sequence
                cur_longest = 0
                for i in range(n, n+len(nums)):
                    if i in s:
                        cur_longest += 1
                    else:
                        break
                longest = max(longest, cur_longest)
                if longest == len(nums):
                    # Short circuit since there cannot be a longer sequence
                    return longest
        return longest
        
