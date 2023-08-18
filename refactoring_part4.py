# this is our initial function
# def is_positive(number):
#     if number >= 0:
#         return True 
#     else:
#         return False 
    
# we can refactor it like this 

def is_positive(number: int)->bool:
    return number>=0

print(is_positive(-8))

