def mydecorator(fun):
    def inner():
        print("Before hellofun")
        fun()
        print("After hellofun")

    return inner

@mydecorator
def hellofun():
    print("Hello")
hellofun()