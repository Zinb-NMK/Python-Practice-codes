#How to do a profile a python script.
import cProfile#This module allows you to track how much time is
# spent on different functions

def sum():
    print(1,3)

cProfile.run('sum()')

'''ncalls: Number of calls made to the function.
tottime: Total time spent in the function itself (excluding calls to sub-functions).
percall: Time per call (calculated as tottime divided by ncalls).
cumtime: Cumulative time spent in the function and all sub-functions.
percall: Time per call for cumulative time.'''