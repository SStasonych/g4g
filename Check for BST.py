# Could be done easily with range, here also getting min max for nodes

class Solution:
    def isBST(self, root: 'Node') -> bool:
        return getMaxMin(root)[0]
    
def getMaxMin(root):
    if root == None: return True, 0, 0
    if root.right != None:
        if root.right.data == root.data: return False,0,0
        res, min1, max1 = getMaxMin(root.right)
    else:
        res, min1, max1 = True, root.data, root.data
    if not res: return False,0,0
    
    if root.left != None:
        if root.left.data == root.data: return False,0,0
        res, min2, max2 = getMaxMin(root.left)
    else:
        res, min2, max2 = True, root.data, root.data
    if not res: return False,0,0
    
    if root.data < max2 or root.data > min1: 
        return False, 0, 0
    
    return True, min2, max1