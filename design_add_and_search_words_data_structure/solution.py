"""
I can solve this problem using a Trie data structure. The Trie will have a series of nodes that store the letters
in each word, as well as which letters follow that letter in a data structure. Formally, each node will contain which
letter that node refers to, whether or not it is the end of a word and what letters follow that letter in the trie.
If both apple and application are in the trie, these words follow the same path from a->p->p->l and then diverge at
l.

Time Complexity:

addWord: O(w) --> w is the length of the word
searchWord: O(w) --> w is the lenth of the word 

Memory Complexity:

addWord: O(w)
time complexity: O(w) --> call stack
"""
class TrieNode:

    def __init__(self, val=None, terminal=False):
        self.val = val
        self.next_letters = {}
        self.terminal = terminal


class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Starting at the head, either iterate through the map of characters the head points to or add a new one
        if the character doesn't exist
        """
        self.__addWordHelper__(word, 0, self.head)
    
    def __addWordHelper__(self, word: str, idx: int, cur: TrieNode) -> None:
        """
        Helper function for addWord. Has additional parameters to track index in word and the current node
        """
        if idx >= len(word):
            cur.terminal = True
            return

        cur_letter = word[idx]
        if cur_letter in cur.next_letters.keys():
            self.__addWordHelper__(word, idx+1, cur.next_letters[cur_letter])
        else:
            new_node = TrieNode(cur_letter)
            cur.next_letters[cur_letter] = new_node
            self.__addWordHelper__(word, idx+1, new_node)
        return

    def search(self, word: str) -> bool:
        """
        Search the trie for the given word. Word can include wild cards
        """
        return self.__searchHelper__(word, 0, self.head)
    
    def __searchHelper__(self, word: str, idx: int, cur: TrieNode) -> bool:
        """
        Helper for search. Iterates through trie to find word. If wildcard, iterate through every letter until the
        word is found or return False. Note for wild cards, there must still be a word of the correct length inserted
        into the Trie for the wild card to match. For example, if the Trie only contains "baby" but the search word is
        "b..", then this function should return False
        """
        if cur.terminal and idx == len(word):
            return True
        elif not cur.terminal and idx == len(word):
            return False
        
        cur_letter = word[idx]
        if cur_letter != '.':
            if cur_letter in cur.next_letters.keys():
                return self.__searchHelper__(word, idx+1, cur.next_letters[cur_letter])
            else:
                return False
        else:
            for l in cur.next_letters.keys():
                found = self.__searchHelper__(word, idx+1, cur.next_letters[l])
                if found:
                    return True
        return False
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
