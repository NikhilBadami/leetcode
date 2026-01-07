class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        I'm given a list of unsorted numbers and need to find the longest consecutive elements sequence. The algorithm needs to run
        in O(n) time, so I cannot sort the array. I need some way to order the elements. Can I hash each number to a list of elements
        that come after it? No, because this would be an O(n^2) algorithm since I'd need to loop over the keys of the map to determine
        which key it should be mapped to. The naive approach would be to sort the array and iterate starting from the beginning.

        Another way to think about this is I know that the longest possible sequence the array could create is the length of the
        array itself. I could then get the minimum and maximum numbers and iterate in a range created by these bounds. On each
        iteration, I check if the current number exists in the map. If it does, I begin counting the length of a sequence. For every
        subsequent number that exists in the map, I continue increasing this counter, but if there is a break, the counter resets.
        One problem with this approach is its not linear in the input of the array. For example, the input (1, 1001, 1002, 1003)
        has an answer of [1001, 1002, 1003] for an array of length 4, but would perform 1004 operations to find the answer since the
        min value is 1.
        """
        longest = 0
        if len(nums) == 0:
            return longest
        s = set()
        for n in nums:
            s.add(n)
        
        _min = min(nums)
        _max = max(nums)
        cur_longest = 0
        for i in range(_min, _max+1):
            if i in s:
                cur_longest += 1
                longest = max(longest, cur_longest)
            else:
                cur_longest = 0
        return longest
        
