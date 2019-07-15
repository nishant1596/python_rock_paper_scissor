#Rock Paper Scissor
from random import randint

print("##Rock Paper Scissor##")
print("Player 1 Turn : ")

player_turn=input().lower()

computer_turn_rand=randint(0,2)
if(computer_turn_rand==0):
    computer_turn='rock'
elif(computer_turn_rand==1):
    computer_turn='paper'
else:
    computer_turn='scissor'
print(f"computer turn : {computer_turn}")
if(player_turn==computer_turn):
    print('Its a Tie')
    quit()
elif(player_turn=='rock'):
    if(computer_turn=='paper'):
        print('Player wins')
    elif(computer_turn=='scissor'):
        print('Player Loses, computer wins')
elif(player_turn=='paper'):
    if(computer_turn=='rock'):
        print('Player Wins')
    elif(computer_turn=='scissor'):
        print('Player Loses, computer wins')
elif(player_turn=='scissor'):
    if (computer_turn == 'paper'):
        print('Player wins')
    elif (computer_turn == 'rock'):
        print('Player Loses, computer wins')
else:
    print('Please provide valid input (Rock/ Paper/ Scissor')