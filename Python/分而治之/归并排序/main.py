# 
# 分解数组

def merge(arr, left, mid, right):
    # 1. 初始化
    # 1.1 确保两个指针 (回忆哑铃增重问题的指针)
    i = left
    j = mid + 1
    k = 0
    arr_copy = arr.copy() # or arr_copy = arr[:]
    while i <= mid and j <= right:
        if arr_copy[i] <= arr_copy[j]:
            arr[left+k] = arr_copy[i]
            k += 1
            i += 1
        else:
            arr[left+k] = arr_copy[j]
            k += 1
            j += 1
    while i <= mid:
        arr[left+k] = arr_copy[i]
        i += 1
        k += 1
    while j <= right:
        arr[left+k] = arr_copy[j]
        j += 1
        k += 1
    

def merge_sort(arr, left, right):
    if left == right:
        return
    mid = (right-left)//2 + left # 取中点
    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)
    merge(arr, left, mid, right)

if __name__ == "__main__":
    import random
    arr = [random.randint(0, 1000) for _ in range(100)]
    print(f'未排序数组\t{arr}')
    left = 0
    right = len(arr) - 1
    merge_sort(arr, left, right)
    print(f'排序数组\t{arr}')