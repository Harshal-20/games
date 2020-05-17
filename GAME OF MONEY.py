import time
print("HELLO, WELCOME TO THE GAME OF MONEY")
print("This is a game in which the game will guess money in your pocket")

ans = input("Are you ready to play ? (y/n): ")

if ans.lower() == 'y':
    print("Take the amount in your pocket")
time.sleep(3.5)
print("Now add 5 to it")
time.sleep(3.5)
print("Now multiply it by 5")
time.sleep(3.5)
print("Now double it")
time.sleep(3.5)
print("Now add any your favorite number from 1 to 10 to it")
time.sleep(3.5)
print("Now add 10 to it")
time.sleep(3.5)
ans = int(input('Now enter the final number: '))
l = len(str(ans))
t = int(str(ans)[-1:])
left = l-1
f = int(str(ans)[:left])
m = f - 6

print('Money in your pocket is:', str(m))