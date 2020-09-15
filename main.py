# Author: Marvin Jakobs mkj5388@psu.edu
# Collaborator: August Sanderson aes6218@psu.edu
# Collaborator: Anthony Cicardo abc6181@psu.edu
# Collaborator: Jian Weng jpw6087@psu.edu
# Section: 1
# Breakout: 2


def sum_n(n):
  if(n <= 0):
    return n
  else:
    return n + sum_n(n-1)

def print_n(s, n):
  if(n <= 0):
    return None
  else:
    print(s)
    print_n(s, n-1)



def run():
  num = int(input("Enter an int: "))
  print("sum is " + str(sum_n(num)) + ".")
  phrase = (input("Enter a string: "))
  print_n(phrase,num)

if __name__ == "__main__":
  run()