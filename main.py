# Author: Marvin Jakobs mkj5388@psu.edu
# Collaborator: August Sanderson aes6218@psu.edu
# Collaborator: Anthony Cicardo abc6181@psu.edu
# Collaborator: Jian Weng jpw6087@psu.edu
# Section: 1
# Breakout: 2


def sum_n(x):
  print(sumCalc(x))

def sumCalc(n):
  if(n <= 0):
    return n
  else:
    return n + sumCalc(n-1)

def print_n(s, n):
  if(n <= 0):
    return None
  else:
    print(s)
    print_n(s, n-1)



def run():
  num = int(input("Enter an int: "))
  print("sum is " + str(sumCalc(num)) + ".")
  phrase = (input("Enter a string: "))
  print_n(phrase,num)

if __name__ == "__main__":
  run()