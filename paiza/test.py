
num = []
n = 152
while n != 0:
  num.append(n % 10)
  n /= 10
  print(n)
num.reverse()

print(num[0])
