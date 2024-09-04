# O(n \log n)

def quick_sort(mas):
    if len(mas) <= 1:
        return mas

    element = mas[0]
    left = list(filter(lambda x: x < element, mas))
    center = [i for i in mas if i == element]
    right = list(filter(lambda x: x > element, mas))

    return quick_sort(left) + center + quick_sort(right)

arr = [12, 11, 13, 5, 6]
arr = quick_sort(arr)

print("Отсортированный массив:", arr)