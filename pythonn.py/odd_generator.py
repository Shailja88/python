#fibonacci
def generate_odd():
    n1=1
   
    while True:
        yield n1
        n1=n1+2


seq=generate_odd()


print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
