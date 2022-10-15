#Rock, Paper Scissors by Joshua Smith
import random
# edited definitions to pass different values through.
# For player names and choices
def PAnswer(P, N):
    while True:
        if int(P) == 1:
            print('{0} picked Rock! '.format(N))
            break
        elif int(P) == 2:
            print('{0} picked Paper! '.format(N))
            break
        elif int(P) == 3:
            print('{0} picked Scissors! '.format(N))
            break
        else:
            print('You must type either 1, 2, or 3. Try again.')
            continue


# function to determine winner
def turnResult(pl, p2):
    if int(pl) == 1 and int(p2) == 1:
        print('   Its a tie...')
    elif int(pl) == 1 and int(p2) == 2:
        print('   Paper beats Rock. {0} wins!'.format(p2Name))
    elif int(pl) == 1 and int(p2) == 3:
        print('Rock beats Scissors. {0} wins!'.format(p1Name))
    elif int(pl) == 2 and int(p2) == 1:
        print('   Paper beats Rock. {0} wins!'.format(p1Name))
    elif int(pl) == 2 and int(p2) == 2:
        print('   Its a tie...')
    elif int(pl) == 2 and int(p2) == 3:
        print('   Scissors beats Paper. {0} wins!'.format(p2Name))
    elif int(pl) == 3 and int(p2) == 1:
        print('   Rock beats Scissors. {0} wins!'.format(p2Name))
    elif int(pl) == 3 and int(p2) == 2:
        print('   Scissors beats Paper. {0} wins!'.format(p1Name))
    elif int(pl) == 3 and int(p2) == 3:
        print('   Its a tie...')


# user input function
def turn(P, N):
    print(str(N) + ', Make your choice! ')
    while True:
        try:
            P = input('  Type 1 for Rock, 2 for Paper, '
                      'or 3 for Scissors:')
        except ValueError:
            print(' You must type a single number.\n')
            continue
        if int(P) != 1 and int(P) != 2 and int(P) != 3:
            print(' You must type either 1, 2, or 3. Try again.\n')
            continue
        elif int(P) == 1 or int(P) == 2 or int(P) == 3:
            return P
        else:
            break


# The actual program begins here
print('Lets play Rock, Paper, Scissors!\n')
p1Name = input('Enter your name: ')
p2Name = 'CPU'
print('')
p1 = 0
p1 = turn(p1, p1Name)
print('')

RPS = [1, 2, 3]
p2 = random.choice(RPS)
print('')
PAnswer(p1, p1Name)
PAnswer(p2, p2Name)
print('')
turnResult(p1, p2)
print('')
end = input('End')