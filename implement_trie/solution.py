"""
One idea is to have a dummy root which holds references to every unique starting letter in the
trie. I.e., if we have the words "apple," "banana," and "orange," the nodes the root holds will
be "a", "b" and "o." When inserting words, words that have the same prefixes will follow the
same path in the tree and only diverge when their letters are different. So, for example, the
words "apple" and "application" will follow the same path a->p->p->l but then diverge at l
which will have references to both the rest of application and the rest of apple
"""
class TrieNode:
        # Private class that holds the current value of the node as well as
        # a map of letters it points to. Includes an init method and an
        # add method to add nodes to its reference list. Additionally,
        # it also includes a method to change a flag indicating if this
        # node is the end of a word

        def __init__(self, val=None, terminal=False):
            self.val = val
            # Note to future self: Do not instantiate objects as a default
            # argument
            self.next_letters = {}
            self.terminal = terminal

class Trie:

    def __init__(self):
        # Create a dummy head that has an empty value and next letters list
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a new word into the Trie. To do this, need to search the existing prefixes
        in the tree and add new letters where relevant, or create a new prefix in the Trie.
        For complexity, worst case time would involve searching every letter map in every
        node where the limiting factor is the number of nodes in the Trie.

        time: O(n)
        memory: O(l) -> l is the length of the word
        """
        return self.__insert_helper__(self.head, word, 0)
    
    def __insert_helper__(self, cur_node: TrieNode, word: str, idx: int) -> None:
        """
        Helper function for insertion. Iterates through the tree to find the correct place
        to insert the new letters of the word. Takes the current node, the overall word
        and the current index in the word.
        """
        if idx >= len(word):
            # End of word
            cur_node.terminal = True
            return
        cur_letter = word[idx]
        # Check to see if the current letter is in the current nodes letter map
        # If so, iterate into that node
        if cur_letter in cur_node.next_letters.keys():
            next_node = cur_node.next_letters[cur_letter]
        else:
            # Create a new node with the letter and add it to the current nodes
            # letter map, then iterate into the new node
            next_node = TrieNode(val=cur_letter)
            cur_node.next_letters[cur_letter] = next_node
        idx += 1
        return self.__insert_helper__(next_node, word, idx)
        

    def search(self, word: str) -> bool:
        """
        Search through tree for the word, letter by letter. If we find a node that does not include
        the current letter or the word has terminated but the current node doesn't indicate this,
        return False. Otherwise, return True

        time: O(n)
        memory: O(l) -> l is the length of the word
        """
        return self.__search_helper__(self.head, word, 0)
    
    def __search_helper__(self, cur_node: TrieNode, word: str, idx: int) -> bool:
        """
        Helper function for search. Iterates through the tree and word and returns True if
        the word is found and False otherwise
        """
        # Check if the idx is out of bounds of the word
        if idx == len(word):
            return cur_node.terminal
        # If the word has not been exhausted but the current letter is not in the current
        # nodes letter map, return false
        if word[idx] not in cur_node.next_letters.keys():
            return False
        next_node = cur_node.next_letters[word[idx]]
        idx += 1
        return self.__search_helper__(next_node, word, idx)

    def startsWith(self, prefix: str) -> bool:
        """
        Similar to search but does not need to check terminal condition, only if the letters
        exist in the tree

        time: O(n)
        memory: O(l) -> l is the length of the word
        """
        return self.__startsWith_helper__(self.head, prefix, 0)
    
    def __startsWith_helper__(self, cur_node: TrieNode, word: str, idx: int) -> bool:
        # Check if the idx is out of bounds of the word
        if idx == len(word):
            if cur_node.val == word[-1]:
                return True
            else:
                # The word was not found
                return False
        # If the word has not been exhausted but the current letter is not in the current
        # nodes letter map, return false
        if word[idx] not in cur_node.next_letters.keys():
            return False
        next_node = cur_node.next_letters[word[idx]]
        idx += 1
        return self.__startsWith_helper__(next_node, word, idx)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
