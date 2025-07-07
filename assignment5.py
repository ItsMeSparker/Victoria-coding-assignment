import doctest
import random

#PartONE
def get_sequence(a: int, b: int, Max: int) -> str:
    """ This function will take the initial number of sequence, the step of 
    sequence, and the maximum number of sequence. The function will return
    the certain sequence in form of string.
    >>> get_sequence(2, 5, 32)
    '2, 7, 12, 17, 22, 27, 32'
    >>> get_sequence(2, 5, 31)
    '2, 7, 12, 17, 22, 27'
    >>> get_sequence(-3, 9, 20)
    '-3, 6, 15'
    >>> get_sequence(-6, 12, 40)
    '-6, 6, 18, 30'
    >>> get_sequence(0, 2, 19)
    '0, 2, 4, 6, 8, 10, 12, 14, 16, 18'
    >>> get_sequence(0, 18, 9)
    '0'
    >>> get_sequence(4, 2, -6)
    '4'
    >>> get_sequence(2, 2, 2)
    '2'
    """
    Result = str(a)
    Last = a
    i = 1
    while Last + b <= Max :
        Result += ', ' + str(a + (b*i)) 
        Last = a + (b*i)
        i += 1
        
    return Result

def digit_sum(digit: int) -> int:
    """ This function will seperate each digit into a single number and sum up
    into one number that will also be returned. It works the same way for both
    positive and negatve numbers.
    >>> digit_sum(-571)
    13
    >>> digit_sum(432)
    9
    >>> digit_sum(0)
    0
    >>> digit_sum(1429)
    16
    >>> digit_sum(11)
    2
    >>> digit_sum(-12416825)
    29
    """
    if(digit < 0):
        digit *= -1
    Sum = 0
    while (digit>=9):
        Sum += digit % 10 #432 -> 2
        digit = digit // 10
    Sum += digit
    
    return Sum

def sum_factors(num: int) -> int:
    """ This function will take an integer and will return the sum of factors
    of that particular number except itself.
    >>> sum_factors(12)
    16
    >>> sum_factors(16)
    15
    >>> sum_factors(10)
    8
    >>> sum_factors(-16)
    0
    >>> sum_factors(0)
    0
    >>> sum_factors(888)
    1392
    >>> sum_factors(7)
    1
    """
    if num<=0: return 0
    
    result = 0
    for i in range(num):
        if i != 0:
            if num%i == 0:
                result = result + i
    return result

def is_perfect(num: int) -> bool:
    """ This function will take an integer and return the boolean that tell if
    that number is perfect number or not. perfect number is the number that its
    factors sum is equal to itself.
    >>> is_perfect(0)
    False
    >>> is_perfect(6)
    True
    >>> is_perfect(28)
    True
    >>> is_perfect(496)
    True
    >>> is_perfect(8128)
    True
    >>> is_perfect(7)
    False
    >>> is_perfect(19)
    False
    >>> is_perfect(77)
    False
    """
    if num<=0: return False
    
    Sum = 0
    for i in range(num):
        if i != 0:
            if num%i == 0:
                Sum = Sum + i 
        
    if Sum == num: return True
    else: return False
    
def n_perfect_numbers(num: int) -> str:
    """ This function will take an integer and use the privious funtion to 
    create and return a string that contain a set of perfect number as much
    index as a taken integer.
    n_perfect_numbers(4)
    '6,28,496,8128'
    n_perfect_numbers(3)
    '6,28,496'
    n_perfect_numbers(2)
    '6,28'
    n_perfect_numbers(1)
    '6'
    n_perfect_numbers(0)
    ''
    """
    if num <= 0: return ''
    Result = ''
    index = 0
    i = 1
    while index < num :
        x = is_perfect(i)
        if x:
            Result = Result + str(i) + ','
            index+=1
        i+=1
    Result = Result[:-1]
    return Result


#PartTWO
MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5


def roll_one_die() -> int:
    """ simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    # this line MUST be uncommented when submitting to PrairieLearn
    die = random.randint(MIN_ROLL, MAX_ROLL)

    # for testing to allow you to enter the dice roll you want at the keyboard
    # comment out the line above and uncomment this line:
    # this line MUST be commented out when submitting to PrairieLearn
    # die = int(input('enter a simulated dice roll\n'))

    return die

def take_turn(name: str, current: int, target: int) -> int:
    """ This function will take name of the player, the current score of the
    player and the target round of the game. in one turn, player will roll the
    dice as many time as it goes, except when the score in that roll is zero or
    the current score is 21 or more. When the turn end, this function will
    return the current score.
    """
    score = 1 #Define score, it is 1 to enter the loop
    print(f"Player {name} is taking a turn in round {target}")
    while(current < 21 and score != 0):
        score = 0 #Reset value of score
        roll = [0,0,0] #Define and reset array of dice rolled
        for i in range(len(roll)):
            roll[i] = roll_one_die()
            if roll[i] == target:
                score += 1
        if roll[0] == roll[1] and roll[1] == roll[2]:
            if score == 3: #This case handle all Three number equal to target
                score = 21
            else: score = 5 #This case handle just all three number equal
        current += score
        print(f"Three dice rolled: {roll}")
        print(f"scored: {score} points")
        print(f"Total points: {current}\n")
    return current

def play_round(player1: str,player2: str, target: int) -> str:
    """ This function will call the privious function to play the entire game
    of Bunko, there will be two player, and will play the game turn by turn
    If one's current score reach 21 before the other, that player wins
    """
    player1_current = 0
    player2_current = 0
    
    while(player1_current < 21 and player2_current < 21):
        player1_current = take_turn(player1, player1_current, target)
        if player1_current < 21: #if players one win, player 2 can't take turn
            player2_current = take_turn(player2, player2_current, target)
       #print(f"DEBUG INSIDE {player1_current} {player2_current}")
    
    #print(f"DEBUG OUTSIDE {player1_current} {player2_current}")
    if player1_current > player2_current:
        winner = player1
    else: winner = player2
    print(f"the winner of this round is: {winner}")
    print(f"{player1} has {player1_current} points and {player2} has {player2_current} points")
    return winner