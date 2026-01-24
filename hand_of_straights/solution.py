class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        I'm given an integer, hand, which contains card numbers and a groupSize that I would like to use to rearrange the hand such that the
        hand can be divided into some number of groups where each group is of size groupSize and each group contains consecutive cards. This means
        that a card hand of [1,1,2] is invalid, but a hand of [1,2,3] is valid. The hand can be given in any order, so it would be useful to
        sort it first before attempting to solve the problem. Additionally, it would be good to see if the length of the hand can be evenly
        divided by groupSize; if it cannot, the problem cannot be solved. Note that consecutive means that the difference between
        consecutive cards can be at most 1

        Assuming a valid grouping is possible, I can iterate through the array and check every groupsize indices if the grouping is valid.
        If any group is invalid, return False, otherwise return True. Note that there could be duplicates. To handle this, I iterate through
        the sorted array and check for each number, assume it is the smallest number in the group. Check if num+1 and num+2 exist in a map that
        is used to count the frequency of each number. If they don't exist, return false. If the count of num+1 or num+2 reaches 0 before
        the current num, return False. Consider the example [1,2,3]. If we are using 1 as the smallest value in this grouping, the only other
        valid values are 2 and 3. If we run out of 2s or run out of 3s, we cannot create any additional groups with 1s and will have left overs.
        This will create invalid groupings.

        time: O(nlog(n))
        memory: O(n)
        """
        # Check to see if the input can even be divided evenly by groupSize
        if len(hand) % groupSize != 0:
            return False
        
        # Sort the input and count the frequency of each number in the input
        hand.sort()
        count = {}
        for n in hand:
            count[n] = count.get(n, 0) + 1
        
        # Iterate through the sorted hand. For each value encountered, treat it as the smallest value in a grouping.
        for n in count.keys():
            # If we are already out of counts for this number, skip
            if count[n] == 0:
                continue
            # Check if we can create a valid grouping by checking if all consecutive numbers starting from n have non-zero counts
            # Additionally, if the count of n is greater than any consecutive number, we cannot create valid groupings because
            # there will be a left over instance of n that cannot be grouped
            for i in range(1, groupSize):
                if n+i not in count.keys() or count[n+i] == 0 or count[n] > count[n+i]:
                    return False
                # If above conditions are false, decrement the count of this number by count[n]
                count[n+i] = count[n+i] - count[n]
            # Finally, set the count of the current number to 0
            count[n] = 0
        return True
        
