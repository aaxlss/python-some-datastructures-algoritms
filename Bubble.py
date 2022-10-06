def bubble(array):
    swap = True
    length = len(array)
    while swap:
        n_1 = None
        n_2 = None
        for i in range(length - 1):
            n_1 = array[i]
            n_2 = array[i + 1]

            if n_1 > n_2:
                tmp = n_2
                array[i + 1] = n_1
                array[i] = tmp
                swap = True
            else:
                swap = False
        length -= 1

    return array 

def main():
    no_sort_array = [8,4,6,2,78,154,756,248,78]
    print(bubble(no_sort_array))

if __name__ == '__main__':
    main()