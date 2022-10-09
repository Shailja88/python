#fibonacci
def generate_fibonacci():
    n1=0
    n2=1
    while True:
        yield n1
        n1 , n2=n2 , n1+n2


seq=generate_fibonacci()


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
print(next(seq))
