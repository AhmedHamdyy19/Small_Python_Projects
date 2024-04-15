# first class function can be treated like any other variable
# higher order functions accept a function as an argument or return function
 
def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):      # higher order function
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

x = [1,2,3,4,5,6]
print(my_map(square, x))         # square is a first class function
print(my_map(cube, x))           # cube is a first class function

#-----------------------------------------------------------------------------

def make_power_func(exponent):  # higher order function
    def power(x):
        return x ** exponent
    return power 

sq = make_power_func(2)          # first class function
print(sq(2), sq(5))

cub = make_power_func(3)
print(cub(2), cub(5))
