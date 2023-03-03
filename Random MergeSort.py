from random import randint

def merge_sort (array):
    if len(array) > 1:
        mid = len(array) // 2
        left_arr = array[:mid]
        right_arr = array [mid:]
        print(f"input dibagi 2 bagian ~~~ {left_arr} dan {right_arr}")

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0       

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1

        while (i < len(left_arr)):
            array[k] = left_arr[i]
            i += 1
            k += 1
        
        while (j < len(right_arr)):
            array[k] = right_arr[j]
            j += 1
            k += 1
        print("output hasil sorting  --- {}". format(array))

array = []
for i in range(10):
    bil = randint(0,100)
    array.append(bil)

print("-"*60)
print("Sebelum di MergeSort", array)
print("-"*60)

merge_sort(array)
print("-"*60)
print("Setelah di MergeSort", array)
print("-"*60)