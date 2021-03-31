def func(arr):
    if len(arr) == 0:
        return 0
    return func(arr[1:]) + arr[0]

if __name__ == '__name__':
    print(func([1, 2, 3, 4, 5]))
