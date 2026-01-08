"""
I need to design a data structure that supports the following:

The data structure needs to support storing multiple values for a single key that are further indexed by timestamp.
I need to be able to retrieve a value from the map either based on an exact timestamp, or, if the timestamp doesn't exist, the most
recent timestamp. Additionally, if there are no values for the key, or the key doesn't exist in the map, return ""

A key can generally map to multiple values by mapping the key to a list. To integrate the timestamp functionality, I can make
the list store tuples of (timestamp, value). All timestamps will be strictly increasing, so appending new values to the end of the
list will mean the list is sorted by timestamp by default. This means I can search for a particular timestamp within the array of
a given key using binary search. If the key doesn't exist, I simply return the last element in this list which represents the most
recently inserted value.

The constructor should initialize a map.

set:
time: O(1) --> Inserting into a map or appending to the end of a list is constant time
memory: O(n)

get:
time: O(log(n))
memory: O(1)
"""
class TimeMap:

    def __init__(self):
        # Initialize map structure
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Add the value to the list stored at the given key. If the key doesn't exist, initialize it and add the value
        """
        if key in self.map.keys():
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        """
        Searches the list at a given key for the value associated with the timestamp. If the key doesn't exist, or the list for
        the key is empty, return an empty string. If the specific timestamp doesn't exist, return the value of the insertion most recent to it.
        For example, if the timestamp being searched for is 11, return the most recent value at timestamp < 11. This means if there is a value
        at timestmap == 12, do not return that value. Otherwise, return the value found at the particular timestamp
        """
        if key not in self.map.keys() or len(self.map[key]) == 0:
            return ""

        # Get the list of values for this key and search for the timestamp. If it doesn't exist, return the most recently added item
        values = self.map[key]
        # Check to see if the current timestamp is before any existing timestamp
        if timestamp < values[0][0]:
            return ""
        
        # Search for the timestamp if it exists
        l, r = 0, len(values) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        # If the timestamp wasn't found using the search above, I need to search for the most recently inserted value such that the timestamp
        # comes before the given timestamp. I'm searching for a value less than the current timestamp. If I find a value less than the current
        # timestmap, I should continue searching as there may be other values closer to the current timestamp. So the upper bound of this search
        # is the input timestamp. My conditions for searching are, if the mid point is greater than the timestmap, search to the left. If it is
        # less than the timestamp, record this value and continue searching. This search operates with the assumption that the given timestamp
        # doest not exist in the array. If it did, it would have been returned by the previous search
        most_recent_timestamp = -1
        most_recent_value = ""
        l, r = 0, len(values) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][0] > timestamp:
                r = mid - 1
            else:
                cur_timestamp, cur_value = values[mid]
                if cur_timestamp > most_recent_timestamp:
                    most_recent_value = cur_value
                    most_recent_timestamp = cur_timestamp
                l = mid + 1
        return most_recent_value



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
