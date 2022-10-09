num_list=[1,4,9]
iter_obj=iter(num_list)

while(True):
    try:
        element=next(iter_obj)
        print(element)
    except StopIteration:
        break