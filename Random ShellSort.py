from random import randint

def shellSort(array, n):
    interval = n // 2 #Memperkecil jarak
    while interval > 0:
        for i in range(interval, n):
            value = array[i] # Mengambil value dari index i
            j = i #Menginisiasi index i
            while j >= interval and array[j - interval] > value:
                array[j] = array[j - interval] #Menginisiasi value index j dengan value dengan index (j-interval)
                j -= interval #Untuk menghentikan perulangan

            array[j] = value #Menginisiasikan value index j dengan value index i
        interval //= 2 #Menentukan jarak lompatan index berdasarkan pembagian panjang data
        print(array)

data = []
for i in range(10):
    bil = randint(0,100)
    data.append(bil)

print("-"*61)
print("Sebelum di ShellSort:", data)
print("-"*61)

size = len(data)
shellSort(data, size)

print("-"*61)
print("Setelah di ShellSort:", data)
print("-"*61)
