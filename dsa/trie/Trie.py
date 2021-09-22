"""
A trie is a special data structure used to store string that can be 
visualized like a graph. Tries are generally used on group of string
rather that a single string.

Use: If you have long string of word tries can help in storing string
in a single tree represent all of the words.

Modified by: Rahul Prajapati
Source: https://www.youtube.com/results?search_query=trie+in+python
"""

class TrieDict:

    def __init__(self):
        self.root = {"*": "*"}

    def insert_word(self, word):

        c_node = self.root

        for letter in word:
            if letter not in c_node:
                c_node[letter] = {}
            c_node = c_node[letter]

        c_node["*"] = "*"

    def has_word(self, word):

        c_node = self.root

        for letter in word:
            if letter not in c_node:
                return False
            c_node = c_node[letter]

        return "*" in c_node

    def has_prefix(self, word):

        c_node = self.root

        for letter in word:
            if letter not in c_node:
                return False
            c_node = c_node[letter]

        return True


class TrieNode:

    def __init__(self, letter):
        self.letter = letter
        self.is_end_of_word = False
        self.children = {}

class Trie:

    """
    Time Complexity:
    
    Insert: O(M)
    Search: O(M)
    
    M is the length of word
    """
    def __init__(self):
        self.root = TrieNode('*')

    def insert_word(self, word):
        c_node = self.root
        for letter in word:
            if letter not in c_node.children:
                c_node.children[letter] = TrieNode(letter)
            c_node = c_node.children[letter]
        c_node.is_end_of_word = True

    def has_word(self, word):
        if word == "":
            return True

        c_node = self.root
        for letter in word:
            if letter not in c_node.children:
                return False
            c_node = c_node.children[letter]

        return c_node.is_end_of_word == True

    def has_prefix(self, word):

        if word == "":
            return True

        c_node = self.root
        for letter in word:
            if letter not in c_node.children:
                return False
            c_node = c_node.children[letter]
        return True


words = ["wait", "waiter", "shop", "shopper"]

trie = TrieDict()

trie.insert_word(words[0])
trie.insert_word(words[1])
trie.insert_word(words[2])
trie.insert_word(words[3])

print(trie.root)

print(trie.has_word("wait"))
print(trie.has_word(""))
print(trie.has_prefix("wa"))
print(trie.has_prefix("waitert"))
print(trie.has_prefix("we"))
