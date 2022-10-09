# num_list=[1,4,9]
# iter_obj=iter(num_list)

# while(True):
#     try:
#         element=next(iter_obj)
#         print(element)
#     except StopIteration:
#         break

class Even:
    def __init__(self,max):
        self.n=2
        self.max=max


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n<=self.max:
            result=self.n
            self.n+=2
            return result

        else:
            raise StopIteration

numbers=Even(10) 
print(next(numbers))
print(next(numbers))
print(next(numbers))
                       
             