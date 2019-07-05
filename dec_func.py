# def do_n_time(func):
#     def wrapper_do_n_time():
#         n = int(input())
#         for i in range(n-1):
#             print("Whee!")
#         func()
#     return wrapper_do_n_time

# def printsomething():
#     print("Whee!")

# printsomething_decorated = do_n_time(printsomething)
# printsomething_decorated()


def do_n_time(func):
    def wrapper_do_n_time():
        n = int(input())
        for i in range(n-1):
            print("Whee!")
        func()
    return wrapper_do_n_time

@do_n_time
def printsomething():
    print("Whee!")

printsomething()




