class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        First, how do I get each elements frequency? I can use a hashmap to hash each element to the number of times
        it occurs in the array. I could convert this map into a list of tuples where each tuple is in the form 
        (freq, el) and then heapify this list. Heapifying a list in python takes O(n) time and retrieving the k
        most frequent elements would take O(klog(k)) time which is technically faster than O(nlog(n))

        time: O(n) to create frequency map and process into tuples
              O(klog(k)) to get top k elements. Worst case O(nlog(n)) if k == n
              total: O(n + klog(k))
        memory: O(n+k)

        import heapq

        # Create frequency map
        freq = {}
        for n in nums:
            if n not in freq.keys():
                freq[n] = 1
            else:
                freq[n] += 1
        
        # Convert the map into list of tuples. By default python creates a min heap when we need a max heap,
        # so have the negative of the freqency be the priority the heap will sort on
        tups = [(-freq[n], n) for n in freq.keys()]

        # Sort the tuples list in O(n) time
        heapq.heapify(tups)

        # Build solution
        res = []
        for i in range(k):
            res.append(heapq.heappop(tups)[1])
        return res
        ******************************************************************************

        There is a way to solve this problem in linear O(n) time by hashing frequencies to arrays of values that
        have that frequency. I know that an element can appear in the array at most n times, in other words, have at
        most n frequency. I can create a map that hashes the frequency of an element to an array of elements that
        have that frequency. I can then iterave through this map in reverse order to find the k most frequency
        elements.

        time: O(n)
        memory: O(n)
        """
        # First create frequency buckets
        freq_buckets = {i: [] for i in range(len(nums) + 1)}

        # Find frequency of each number in list
        freq = {}
        for n in nums:
            if n not in freq.keys():
                freq[n] = 1
            else:
                freq[n] += 1
        
        # Process element frequencies into buckets
        for n in freq.keys():
            f = freq[n]
            # Use the frequency of the number to find the bucket the number goes into
            freq_buckets[f].append(n)

        # Now iterate from n to 0 and find the k most frequency elements
        res = []
        for i in range(len(nums), -1, -1):
            if len(freq_buckets[i]) > 0:
                for el in freq_buckets[i]:
                    res.append(el)
                    k -= 1
                    if k == 0:
                        break
            if k == 0:
                break
        return res
