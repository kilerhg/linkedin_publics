# Defining the Decorator Function
def timer(func):
    # Importing the datetime module
    from datetime import datetime
    # Defining the wrapper function
    def wrapper(*args, **kwargs):
        # print the function name
        print(f"Function Name: {getattr(func, '__name__')}")
        start = datetime.now() # start time
        func(*args, **kwargs) # calling the function
        end = datetime.now() # end time
        time_to_run = end - start # time to run
        # print the time to run
        print(f'Time to run: {time_to_run}')
    return wrapper


@timer # Decorator
# Defining the function which will be decorated
# in this case, I create an example of one
def wait_5_seconds(): 
    # Here you write the code to get the time to run
    from time import sleep
    sleep(5)

wait_5_seconds() # calling the function