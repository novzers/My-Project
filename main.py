# Implement factorial function
def factorial(n):
  sum = 1
  for i in range(1,n+1):
    sum *= i
  return sum

def main():
  print("main here")
  print(factorial(4))
  
if __name__ == '__main__':
  main()
