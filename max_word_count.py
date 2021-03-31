def func(arr):
    if len(arr) == 0:
        return {}
    else:
        result = func(arr[1:])
        if arr[0][0] in result.keys():
            if result.get(arr[0][0]) < len(arr[0]):
                result[arr[0][0]] = len(arr[0])
        else:
            result[arr[0][0]] = len(arr[0])
        return result


if __name__ == '__main__':
    arr = ["aa", "aaa", "aaaaa", "b", "bbbb"]
    print(['{} -> {}'.format(k * v, v) for k, v in func(arr).items()])