from random import randint

def partition(l,bwh,atas): #Melakukan quicksorting pada setiap partisi yang telah dibagi
    print("list    : ", l)
    pivot = l[atas]
    index = bwh
    current = bwh
    print("pivot   : ", pivot)
    while(current < atas):
        if l[current] <= pivot:
            l[index],l[current] = l[current],l[index] #Swapping antara value[index] dan value[current]
            index += 1
        current += 1
    l[index],l[atas] = l[atas],l[index] #Swapping antara value[pivot] dan value[index]
    print("partisi : ", l, "\n")
    return index

def quicksort(l, bwh, atas): #Melakukan pembagian partisi
  if bwh < atas:
    index = partition(l, bwh, atas) #mendapatkan index untuk membagi partisi
    quicksort(l, bwh, index-1) #quicksorting partisi kiri (lebih kecil dari pivot)
    quicksort(l, index+1, atas) #quicksorting partisi kanan (lebih besar dari pivot)
    return l
    
arr = []
for i in range(10):
    bil = randint(0,100)
    arr.append(bil)

print("-"*60)
print(f"Sebelum di QuickSort {arr}")
print("-"*60)

result = quicksort(arr, 0, len(arr)-1)

print("-"*60)
print(f"Setelah di QuickSort {result}")
print("-"*60)