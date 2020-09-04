class Node:
    def __init__(self, key):
        self.val = key
        self.height = 1
        self.left = None
        self.right = None
    
class Tree_Set:

    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        balance = self.get_balance(root)
        
        if balance > 1:
            if key < root.left.val:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        elif balance < -1:
            if key < root.right.val:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
            else:
                return self.rotate_left(root)
        
        return root
    
    def delete(self, root, key):
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_val(root.right)
            root.val = temp
            root.right = self.delete(root.right, temp)
        
        if not root:
            return root
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        balance = self.get_balance(root)
        
        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        elif balance < -1:
            if self.get_balance(root.right) >= 0:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
            else:
                return self.rotate_left(root)
            
        return root
        
    def get_min_val(self, root):
        if not root.left:
            return root.val
        return self.get_min_val(root.left)
    
    def rotate_left(self, z):
        y = z.right
        T = y.left
        y.left = z
        z.right = T
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    
    def rotate_right(self, z):
        y = z.left
        T = y.right
        y.right = z
        z.left = T
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
        
    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right)
    
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    
    def pre_order(self, root):
        if not root:
            return
        print(root.val, end = " ")
        self.pre_order(root.left)
        self.pre_order(root.right)
    
    def get_ceil(self, root, target):
        min_diff, val = inf, None
        while root:
            if target <= root.val:
                diff = root.val - target
                if diff < min_diff:
                    min_diff = diff
                    val = root.val
                root = root.left
            elif target > root.val:
                root = root.right
        return val
    
    def get_floor(self, root, target):
        min_diff, val = inf, None
        while root:
            if target < root.val:
                root = root.left
            elif target >= root.val:
                diff = target - root.val
                if diff < min_diff:
                    min_diff = diff
                    val = root.val
                root = root.right
        return val
        
    

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bst = Tree_Set()
        root = None
        for i in range(len(nums)):
            big, small = bst.get_ceil(root, nums[i]), bst.get_floor(root, nums[i])
            if big != None and big - nums[i]  <= t:
                return True
            if  small != None and nums[i] - small <= t:
                return True
            root = bst.insert(root, nums[i])
            if i+1 > k:
                root = bst.delete(root, nums[i-k])

        return False
