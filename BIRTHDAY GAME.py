import time
import math
print("Hello to Guess the birthday game")

ans = input("Are you to play (y/n) ")

if ans.lower() == 'y':
    print("Take number of the month in which your birth day is E.G if born in january take 1")
time.sleep(3.0)
print("Now double the number of the month")
time.sleep(3.0)
print("Now add 5 to it")
time.sleep(3.0)
print("Now multiply the number by 5")
time.sleep(3.0)
print("Now put zero after the answer")
time.sleep(3.0)
print("Now add date of birth to the answer E.G if born on 23 add 23 + answer")
time.sleep(3.0)
ans = int(input('Now enter the final number: '))
l = len(str(ans))
a = int(str(ans)[-2:])
b = a - 50
left = l-2
f = int(str(ans)[:left])
m = f-2
print('Date of birth is: ', str(b) + ' & Month of birth is: ', str(m))

