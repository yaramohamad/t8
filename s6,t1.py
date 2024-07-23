n=int(input('enter the range:'))
def Fibonacci(f):
 if f == 0:
  return 0
 elif f==1:
  return 1
 else:
  return Fibonacci(f-2) + Fibonacci(f-1) 
for i in range(n):
    print(Fibonacci(i))