import random

# todo, please rewrit below game in with define one or two function

computers_number = random.randint(1,100);
prompt = "what's your guess?"

while True:
    player_guess=input(prompt)
    if computers_number == int (player_guess):
        print("correct!")
        break
    elif    computers_number > int(player_guess):
        print("too small!")
    else:
        print("Too big!")
