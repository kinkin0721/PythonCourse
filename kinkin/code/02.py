def my_range(n):
    idx = list()
    count = 0
    while count < n:
        idx.append(count)
        count += 1

    return idx


def my_range(start, end, step):
    pass


if __name__ == "__mian__":
    my_range(1,8,2)
    [1,3,5,7]