def reverse(string):
    return string[::-1]

def reverseBFWithFor(string):
    new_string = ''
    for i in range(len(string)):
        new_string = string[i] + new_string

    return new_string

def reverseBDWithWhile(string):
    new_string = ''
    max_length = len(string) - 1
    while max_length >= 0:
        new_string += string[max_length]
        max_length -= 1

    return new_string
"""
string = 'querty' => 'uerty' => 'erty' => 'rty' => 'ty' => 'y'

new_string = ''
"""
def reverseWithRecursion(string):
    if len(string) == 0:
        return string
    else:
        return reverseWithRecursion(string[1::] )+ string[0]
def main():
    string = 'querty'
    # print (reverse(string))
    # print (reverseBFWithFor(string))
    # print (reverseBDWithWhile(string))
    print (reverseWithRecursion(string))

if __name__ == '__main__':
    main()