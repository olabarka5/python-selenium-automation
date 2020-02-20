N = int (input ("введите число"))
sum = 0
while N >0:
      d = N%10
      N = N// 10
      sum+= d
print ("сумма всех чисед этого числа=", sum)


