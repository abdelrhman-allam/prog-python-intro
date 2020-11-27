# User function Template for python3

'''
class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
'''


def insert(root, key):
    '''
    root: root of trie tree
    key:  key to be inserted
    '''
    node = root
    for char in key:
        i = charToIndex(char)
        if i not in node.children:
            node.children[i] = TrieNode()
        node = node.children[i]
    node.isEndOfWord = True


def printTrie(root):
    if root == None:
        return
    print('root: ', root, 'len: ', len(root.children))

    for i in range(len(root.children)):
        if root.children[i] != None:
            print('children: ', i)
            printTrie(root.children[i])


def search(root, key):
    '''
    root:       root of trie tree
    key:        key to be searched
    Returns:    true if key presents in trie, else false
    '''
    printTrie(root)
    node = root
    for char in key:
        i = charToIndex(char)
        if i in node.children:
            node = node.children[i]
        else:
            return 0
    return node.isEndOfWord


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
class TrieNode:

    def __init__(self):
        self.children = [None]*26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = TrieNode()

# use only 'a' through 'z' and lower case


def charToIndex(ch):
    return ord(ch)-ord('a')


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())
        arr = 'the a there answer any by bye their'.strip().split()
        strs = 'the'

        t = Trie()

        for s in arr:
            insert(t.root, s)

        if search(t.root, strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends
# the a there answer any by bye their
