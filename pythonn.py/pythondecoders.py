# def inc(x):
#     return x+1

# def operate(fun,x):
#     result=fun(x)
#     return result

# print(operate(inc,3))

# def print_msg(message):
#     greeting="Hello"

#     def printer():
#         print(greeting, message)

#     printer()

# print_msg("Python is awesome")




# def printer():
#     print("Hello world!")

# def display_info(func):

#     def inner():
#         print("Executing",func.__name__, "function")
#         func()
#         print("Finished execution")
       
#     return inner
# # printer()
# decorated_func= display_info(printer)
# decorated_func()


# def display_info(func):

#     def inner():
#         print("Executing",func.__name__, "function")
#         func()
#         print("Finished execution")
       
#     return inner

# @display_info    
# def printer():
#     print("Hello world!")

# printer()


# # printer()

# def smart_divide(func):
#     def inner(a,b):
#         print("Dividing",a,"by",b)
#         if b==0:
#             print("cannot divide by 0!")
#             return 
#         return func(a,b)
#     return inner
# @smart_divide
# def divide(a,b):
#     return a/b

# value1=divide(15,3)
# print(value1)

# value2=divide(5,0)
# print(value2)
