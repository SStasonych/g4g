class Trie():
    def __init__(self):
        self.left = None
        self.right = None
    
    def add(root, arr):
        m = len(arr)
        for i in range(m):
            if arr[i] == 0:
                if not root.left:
                    root.left = Trie()
                root = root.left
            else:
                if not root.right:
                    root.right = Trie()
                root = root.right
    
    def contains(root, arr)-> bool:
        for num in arr:
            if num == 0 and root.left:
                root = root.left
            elif num == 1 and root.right:
                root = root.right
            else:
                return False
        return True
    
class Solution:
    def uniqueRow(self, mat):
        n = len(mat)
        res = []
        t = Trie()
        for i in range(n):
            if Trie.contains(t, mat[i]): 
                continue
            else:
                Trie.add(t, mat[i])
                res.append(mat[i])
                
        return res
        