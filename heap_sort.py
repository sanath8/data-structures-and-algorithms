from random import *
from time import *

def greatest(arr, parent, left, right):
    try:
        if(arr[parent] > arr[left]):
            if(arr[parent] > arr[right]):
                return parent
            else:
                return right
        else:
            if(arr[right] < arr[left]):
                return left
            else:
                return right
    except IndexError:
        try:
            if(arr[parent] < arr[left]):
                return left
            else:
                return parent
        except IndexError:
            return parent


def swap(arr, parent, left, right):
    greatest_node = greatest(arr, parent, left, right)
    temp = arr[greatest_node]
    arr[greatest_node] = arr[parent]
    arr[parent] = temp
    return arr, greatest_node
    
def get_left_child(node):
    return 2*node + 1

def get_right_child(node):
    return 2*node + 2

def heapify(arr):
    ts = time()
    n = len(arr) - 1
    parent = int((n+1)/2) - 1
    while parent >= 0:
        left_child = get_left_child(parent)
        right_child = get_right_child(parent)
        arr, affected_node = swap(arr, parent, left_child, right_child)
        arr = maintain_heap(arr, affected_node)
        parent -= 1
    return arr

def maintain_heap(heap, affected_node):
    while(affected_node != greatest(heap, affected_node, get_left_child(affected_node), get_right_child(affected_node))):
        heap, affected_node = swap(heap, affected_node, get_left_child(affected_node), get_right_child(affected_node))
    return heap

def get_max_item(heap, n):
    max_item = heap[0]
    last_node = heap[n-1]
    heap[0] = last_node
    heap.pop()
    heap = maintain_heap(heap, 0)
    return max_item, heap




arr = [randint(0, 500) for i in range(10000)]
n = len(arr)
t1 = time()
heap = heapify(arr)
sorted_heap = []
for i in range(n):
    maxi, heap = get_max_item(heap, n-i)
    sorted_heap.append(maxi)
t2 = time()


print("Execution Time: ", t2-t1)
print("Sorted list", sorted_heap)


