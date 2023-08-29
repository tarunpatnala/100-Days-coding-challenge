#Functions and While loop


def my_function():
    print("Hello")

my_function()

if __name__ == "__main__":
    my_function()
   #while
    count = 6
    while count > 0:
        print("Hello "+str(count))
        count -= 1
    #do-while
    x = 10
    while True:
        print("bye "+str(x))
        x -= 1
        if x <= 0:
            break