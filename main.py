# Implement factorial function
def factorial(n):
  sum = 1
  for i in range(1,n+1):
    sum *= i
  return sum

def main():
  print("main here")
  n = int(input("Masukkan angka: "))
  print("Hasil faktorialnya: ",end='')
  print(factorial(n))
  
if __name__ == '__main__':
  main()
