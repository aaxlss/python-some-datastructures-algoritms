def selecting(array):
    length = len(array)
    pointer = 0
    
    while pointer < length:
        smallest_index = pointer
        for i in range(pointer + 1,length):
            
            if array[i] < array[smallest_index]:
                smallest_index = i
        tmp = array[pointer]
        array[pointer] = array[smallest_index]
        array[smallest_index] = tmp
        pointer += 1

    return array
def main():
    no_sort_array = [8,4,6,2,78,154,756,248,78]
    print(selecting(no_sort_array))

if __name__ == '__main__':
    main()