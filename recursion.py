# using recursion to implement power and factorial functions

def power(num, pwr):
  if pwr = 0:
    return 1
  else:
    return num * pwr(num, pwr - 1)

def factorial(num):
  if num == 0:
    return 1
  else:
    return num * factorial(num - 1)