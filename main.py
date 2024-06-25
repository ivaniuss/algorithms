def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def main():
    array = [5, 2, 4, 6, 1, 3]
    print(insertion_sort(array))

if __name__ == "__main__":
    main()