def mergeSort(array):
    print(f'array: {array}')
    if len(array) == 1:
        return array
    lenght =  len(array)
    half = int(lenght / 2)
    print(f'half: {half}' )
    print(f'left: {array[:half:]}')
    print(f'right: {array[half:lenght:]}')

    return merge( mergeSort(array[:half]), mergeSort(array[half:]))

def merge(left, right):
    print(f'left: {left}, right: {right}')
    new_array = []
    index_left = 0
    index_right = 0

    while index_left < len(left) or index_right < len(right):

        if index_left >= len(left):
            new_array.append(right[index_right])
            index_right += 1
        elif index_right >= len(right):
            new_array.append(left[index_left])
            index_left += 1
        elif left[index_left] < right[index_right]:
            new_array.append(left[index_left])
            index_left += 1
        else:
            new_array.append(right[index_right])
            index_right += 1

    print(f'ordered array: {new_array}')
    
    return new_array


def main():
    no_sort_array = [8,4,6,2,78,154,756,248,78]
    print(mergeSort(no_sort_array))

if __name__ == '__main__':
    main()