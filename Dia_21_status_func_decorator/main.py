import logging

logging.basicConfig(level=logging.DEBUG)



def memory_used_variable(variable):
    from sys import getsizeof
    # value in mb
    value = float(getsizeof(variable)/1048576)
    return value


def actual_memory_allocate(var_locals):
    list_memory = []
    for variable in var_locals.keys():
        list_memory.append(memory_used_variable(variable=variable))
    total = round(sum(list_memory),5)
    return total


# Defining the Decorator Function
def status_func(func):
    from datetime import datetime
    # import logging
    def wrapper(*args, **kwargs):
        # print the function name
        logging.debug(f"Function Name: {getattr(func, '__name__')}")
        start = datetime.now() 
        func(*args, **kwargs)
        end = datetime.now() 
        time_to_run = end - start
        memory_used = actual_memory_allocate(var_locals=locals())
        logging.debug(f'Time to run: {time_to_run}')
        logging.debug(f'Total memory used: {memory_used}')
    return wrapper


@status_func
def massive_data():
    # total_list_values = []
    # for num in range(100):
    list_values = list(range(10**8))
    list_values *= 10
    unique_values = set(list_values)
    for item in unique_values:
        item *= item
        # total_list_values.append(list_values)

massive_data() # calling the function