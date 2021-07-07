"""
input: n
number of squares: n + 1
output: sum of perimeters of n + 1 squares 

process:
create a list of the side lengths of each square,
i.e. a fibonacci sequence of length n + 1
sum of the list * 4
"""


def generate_fib(n):
    fib = []
    i = 1

    while i < n + 1:
        if i == 1:
            fib = [1]
            i += 1
        elif i == 2:
            fib = [1, 1]
            i += 1
        else:
            fib.append(fib[(i - 1) - 2] + fib[(i - 1) - 1])
            i += 1
    
    return fib


def perimeter(n):
    side_lengths = generate_fib(n + 1)

    return sum(side_lengths) * 4

    # return sum(generate_fib(n + 1)) * 4


print(perimeter(5))