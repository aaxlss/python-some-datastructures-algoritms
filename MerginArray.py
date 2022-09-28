from genericpath import exists


def mergin(array_1, array_2):
    new_array = []
    current_position = 0
    position_array_1 = 0
    position_array_2 = 0

    """
    0 = 0 => 1 = 3 => 2 = 4 => 3 = 31
    0 = 4 => 1 = 6 => 2 = 30 => 3 = null


    [0,3,4, 4, 6, 30, 31]
    """
    while position_array_1 < len(array_1)  or position_array_2 < len(array_2)  :
        
        if not position_array_2 < len(array_2)  or ( array_1[position_array_1] is not None and (array_1[position_array_1] < array_2[position_array_2])):
                print(f'position array 1: {position_array_1} value: {array_1[position_array_1]}')
                new_array.append(array_1[position_array_1])
                position_array_1 += 1
        else:
            print(f'position array 2: {position_array_2} value: {array_2[position_array_2]}')
            new_array.append( array_2[position_array_2])
            position_array_2 += 1
        current_position += 1

    return new_array

def main():
    array_1 = [0,3,4,31]
    array_2 = [4,6,30]

    print(mergin(array_1=array_1, array_2=array_2))


if __name__ == '__main__':
    main()