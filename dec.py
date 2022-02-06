def more_func(func):
    def inner(a, b):
        if b == 0:
            print("error")
            return
        func(a, b)
    return inner


@more_func
def div(a, b):
    print(a/b)


div(1, 10)
