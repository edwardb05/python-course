import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Understanding decorators

def speed_calc_decorator(function):
    def wrapper():
        start_time=time.time()
        function()
        end_time=time.time()
        time_taken = end_time-start_time
        print(time_taken)
    return wrapper #Must return the wrapper function as when it is called it replaces the fast_function
 

@speed_calc_decorator # "@" calls the decorator function and replaces your function
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()#Calls the new wrapped function which gives time as well
slow_function()


