from random import randint

print('Rock-Paper-Scissor Game')
print('=======================')

weapon = ['rock', 'paper', 'scissors']
computer = weapon[randint(0,2)]

print("What weapon do you want to use?")
print("Rock / Paper / Scissors")
player = input().lower()

if computer == player:
    print('draw')
    print('no body wins')
elif player == 'rock':
    print(f'player:{player}')
    print(f'computer:{computer}')
    if computer == 'paper':
       print('computer win!')
    elif computer == 'scissors':
        print('player win')
elif player == 'paper':
    print(f'player:{player}')
    print(f'computer:{computer}')
    if computer == 'scissors':
       print('computer win!')
    elif computer == 'rock':
        print('player win')
elif player == 'scissors':
    print(f'player:{player}')
    print(f'computer:{computer}')
    if computer == 'rock':
       print('computer win!')
    elif computer == 'paper':
        print('player win')