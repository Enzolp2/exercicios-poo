
### BINARY SEARCH ###
# O(log(n))

def binary_search(arr, target):
    l, r = 0, len(arr)
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

valores_ordenados = [2, 6, 7, 10, 11, 12, 13, 14, 19, 20, 21, 22, 25, 26]
alvo = 12
print(binary_search(valores_ordenados, alvo))
