class NumArray:

    def __init__(self, nums: List[int]):
        self.a_size = len(nums)
        if not self.a_size:
            return None
        self.s_size = 2*pow(2, ceil(log(self.a_size, 2))) - 1
        self.s_tree = [0 for i in range(self.s_size)]
        self.arr = nums
        self.construct(self.arr, self.s_tree, 0, self.a_size-1, 0)

        
    def construct(self, arr, s_tree, low, high, node) -> None:
        if low == high:
            s_tree[node] = arr[low]
            return s_tree[node]
        mid = (low+high)//2
        s_tree[node] = self.construct(arr, s_tree, low, mid, 2*node+1) + self.construct(arr, s_tree, mid+1, high, 2*node+2)
        return s_tree[node]
            
    def do_update(self, arr, s_tree, val, ind, low, high, node):
        if low == high:
            arr[ind] = val
            s_tree[node] = val
            return s_tree[node]
        mid = (low+high)//2
        if low <= ind and ind <= mid:
            self.do_update(arr, s_tree, val, ind, low, mid, 2*node+1)
        else:
            self.do_update(arr, s_tree, val, ind, mid+1, high, 2*node+2)
        s_tree[node] = s_tree[2*node+1] + s_tree[2*node+2]
        return s_tree[node]
            
    
    def update(self, i: int, val: int) -> None:
        self.do_update(self.arr, self.s_tree, val, i, 0, self.a_size-1, 0)

        
    def getSum(self, s_tree, low, high, left, right, node):
        if low >= left and high <= right:
            return s_tree[node]
        elif low > right or high < left:
            return 0
        else:
            mid = (low+high)//2
            return self.getSum(s_tree, low, mid, left, right, 2*node+1) + self.getSum(s_tree, mid+1, high, left, right, 2*node+2)

    
    def sumRange(self, i: int, j: int) -> int:
        return self.getSum(self.s_tree, 0, self.a_size-1, i, j, 0)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
