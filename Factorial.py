def factorialRecursive(number):
    if number == 2:
        return number
    else:
        return number * factorialRecursive(number - 1)

def fibonacciRecursive(iteration):

    if iteration < 2:
        return iteration
    else:
        return fibonacciRecursive(iteration - 1) + fibonacciRecursive(iteration - 2)


if __name__ == '__main__':
    # print(factorialRecursive(5))
    print(fibonacciRecursive(43))