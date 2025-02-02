#Use a decorator to obtain positional args no matter how many, then call function
def logging_decorator(function):
    def wrapper(*args):
        print(f'You called a_function{args}')
        sum = function(*args)
        print(f'It returned: {sum}')
    return wrapper



#Using the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)