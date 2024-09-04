# o(1) - константная сложность


def get_element(array, count):
    return array[count-1]

array = [3,7,4,2,6,9]
print(get_element(array, 4))
print("\n")


# o(n) - линейная сложность

def line_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

print(line_search(array, 4))
print(line_search(array, 8))
print("\n")

# o(log(n)) - логарифмическая сложность

def binary_search(array, target):
   low, high = 0, len(array) - 1
   while low <= high:
       mid = (low + high) // 2
       if array[mid] == target:
           return mid
       elif array[mid] < target:
           low = mid + 1
       else:
           high = mid - 1
   return -1

print(binary_search(array, 4))
print(binary_search(array, 8))
print("\n")









