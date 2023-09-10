# open_list = ["[", "{", "("]
# close_list = ["]", "}", ")"]
#
#
# # Function to check parentheses
# def check(myStr):
#     stack = []
#     for i in myStr:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if (len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1]):
#                 stack.pop()
#             else:
#                 return "Unbalanced"
#     if len(stack) == 0:
#         return "Balanced"
#     else:
#         return "Unbalanced"
#
#
# # Driver code
# string = "{[]{()}}"
# print(string, "-", check(string))
#
# string = "[{}{})(]"
# print(string, "-", check(string))
#
# string = "((()"
# print(string, "-", check(string))

def check(test_string):
    brackets = ["()", "{}", "[]"]
    while any(x in test_string for x in brackets):
        for br in brackets:
            test_string = test_string.replace(br, "")
    return not test_string


test1 = "[{}[]{()}]"
test2 = "({}[{}])"
test3 = "{([])}{(})"

print(f"{test1} = {'Balanced' if check(test1) else 'Unbalanced'}")
print(f"{test2} = {'Balanced' if check(test2) else 'Unbalanced'}")
print(f"{test3} = {'Balanced' if check(test3) else 'Unbalanced'}")
