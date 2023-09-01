#Function with Output

def calc(f_name, l_name):

    def val(f_name, l_name):
        #Doc string
        """Take first and last name and format it to return the title case version of the name"""
        output = []
        output.append(f_name.title())
        output.append(l_name.title())
        return (" ".join("{}".format(k) for k in output))
    
    return val(f_name,l_name)
    

print(calc("tARun", "PaTNAla"))

tup = ("Tarun", 1, 231.23)
print(tup[1])

# Calculator

def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2

operations = {"+":add, "-":subtract, "*":multiply, "/":divide}

def calculator():
    num1 = float(input("What's the first number?: "))

    for k in operations:
        print(k)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()