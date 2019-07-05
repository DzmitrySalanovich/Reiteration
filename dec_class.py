def do_n_time(func):
    def wrapper_do_n_time():
        n = int(input())
        for i in range(n):
            print("Whee!")
        func()
    return wrapper_do_n_time


@do_n_time
class deco:
    def printsomething(self):
        print("Whee!")

deco()