class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TreeNode()
            current = current.children[c]
        current.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            current = root
            for i in range(j,len(word)):
                if word[i] == '.':
                    for child in current.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                elif word[i] in current.children:
                    current = current.children[word[i]]
                else:
                    return False
            return current.word
        return dfs(0, self.root)    

        
