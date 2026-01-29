class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        I'm given a string and I need to partition it such that each letter appears in at most one part. For example, the string ababcc can be
        partitioned into abab, cc but not ab, ab, cc because a and b appear in more than one partition. Additionally, the partitioning should
        be done in such a way that if the partitions were joined in order, the original string would be recovered. I need to do return the
        lengths of each partitioned string, not the strings themselves.

        How can I determine how to partition the strings? One way could be to expand a window counting the frequency of each character in the
        window. But I am trying to make sure all occurrences of a single character appear in only one partition. A brute force solution
        would be to try every partition and ensure there are no overlaps in the sets of characters that exist in each partition but this would
        likely time out since the maximum size of the input is 500 (2^500 ~ e150).

        I could work backwards starting at the end of the string and check on each iteration, if I remove the character at the end of the string,
        does it no longer appear in the subsequent string after it. If so, I can create a partition there. Take the exampel ababcc. I start at
        the second c and remove it. I am left with the strings ababc and c. Since c still appears in the first string, this is not a valid
        partition. I then move to the second c and remove it. I am left with abab, cc. I can see that not characters in the second string appear
        in the first string, so I can partition here. I continue this process, now only considering the original string minus the partition
        and see that I cannot partition the string such that any partition would have a unique set of characters.

        Algorithmically, this looks like the following: I start with a pointer at the end of the string and partition on this pointer, i.e.,
        every character at this pointer and beyond forms one string and every character before this pointer forms another string. I then
        perform two loops to create sets of characters in each substring. I take the intersection of these sets and if it is empty, I can
        partition the string. This requires looping over the entire set of characters once per character in the string so the time would be
        O(n^2). I also could potentially split the string once per character, creating copies of size n each time, using n^2 memory. Additionally
        I use memory for each set but this is also n^2

        time: O(n^2)
        memory: O(n^2)
        """
        # Use a deque to track the solution since appending left is efficient
        from collections import deque
        res = deque()
        for i in range(len(s) - 1, 0, -1):
            # Partition the string
            s1 = s[:i]
            s2 = s[i:]
            # Create sets of characters for each substring
            set1 = set()
            for c in s1:
                set1.add(c)

            set2 = set()
            for c in s2:
                set2.add(c)
            # Check that the intersection of these sets is empty
            if len(set1 & set2) == 0:
                res.appendleft(len(s2))
                # Remove the valid substring
                s = s1
        # Finally need to add length of remaining string
        res.appendleft(len(s))
        return list(res)

