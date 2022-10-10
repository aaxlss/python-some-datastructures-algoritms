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
# 
# 0,1,1,2,3,5,8,13,21,34
def fibonacciMemoization(iteration):
    a = 0
    b = 1
    for i in range(iteration -1):
        tmp = b
        b = a + b
        a = tmp
    return b

if __name__ == '__main__':
    # print(factorialRecursive(5))
    # print(fibonacciRecursive(8))
    print(fibonacciMemoization(43))