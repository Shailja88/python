# def even_generator():
#     n=0

#     n+=2
#     yield n

#     n+=2
#     yield n

#     n+=2
#     yield n

# numbers=even_generator()
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

def even_generator(max):
    n=2
    while n<=max:
        yield n
        n+=2
    

numbers=even_generator()
print(next(numbers))
print(next(numbers))
print(next(numbers))