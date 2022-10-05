def factorialRecursive(number):
    if number == 2:
        return number
    else:
        return number * factorialRecursive(number - 1)

if __name__ == '__main__':
    print(factorialRecursive(5))
