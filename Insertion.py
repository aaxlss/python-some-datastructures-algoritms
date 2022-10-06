def insertion(array):
    new_list = []

    if array[0] < array[1]:
        new_list = [array[0], array[1]]
    else:
        new_list = [array[1], array[0]]

    for i in range(2, len(array)):
        current_value = array[i]
        print(current_value)
        for j in range(len(new_list)):
            if current_value < new_list[j]:
                new_list.insert(j, current_value)
                break
            elif j == len(new_list) - 1:
                new_list.insert(j+1,current_value)

        


    return new_list

def main():
    no_sort_array = [8,4,6,2,78,154,756,248,78]
    print(insertion(no_sort_array))

if __name__ == '__main__':
    main()