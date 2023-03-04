def add_and_multiply(x, y):
  # add x and y and store the result in a variable
  sum = x + y
  # multiply x and y and store the result in another variable
  product = x * y
  # return the sum of sum and product
  return sum + product

import math # import the math module

def is_perfect_square(n):
  # check if n is a non-negative integer
  if isinstance(n, int) and n >= 0:
    # calculate the square root of n
    root = math.sqrt(n)
    # check if the square root is an integer
    return root == int(root)
  else:
    # return False for invalid input
    return False
