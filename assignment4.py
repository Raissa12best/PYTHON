def is_perfect_number(number):
  total = 0
  for i in range(1,number):
      if number % i == 0:
         total += i
  return total == number

for num in range(1, 1000000):
   if is_perfect_number(num):
       print(num)

