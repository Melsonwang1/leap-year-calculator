currentyear = int(input('plese put your current year :'))
if (currentyear % 400 == 0) or (currentyear % 100 == 0) and (currentyear % 4 ==0):
 print('it is a leap year')
else:
   print('it is not a leap year')
