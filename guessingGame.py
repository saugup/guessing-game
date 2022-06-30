import random
number = random.randint(1,9)
chances = 1
print("please enter a number")
while chances <= 5:
    player = int(input())
    if number==player:
        print('Congrats! You have won')
        break
    if number<player:
        print('please pick a lower number than',player)
    else:
        print('please pick a higher number than',player)
    chances = chances +1
