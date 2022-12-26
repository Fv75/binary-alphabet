# check if we're in a valid round (1-10)
# get a level from the user
# check that the level is valid and between 1-3
# generate 2 random numbers and print them as an addition to the user
# check if the users answer is correct
# check if they have answered wrong more than 3 times
# add to score
# add to round

import random


def main():
    round = 1
    score = 1
    answers = 1

    level = get_level(input("Level: "))
    while round < 9:
        x, y  = generate_integer(level)
        answer = input(f"{x} + {y} = ")
        while answer < 3:    
                if answer  == x+y:
                round =+ 1
                score =+ 1
                continue
            elif ValueError:
                answer =+ 1
                pass
            else:
                answer =+ 1
                continue


# get user input and make sure it is convertable to int between 1-3
def get_level(x):
    try:
        x=int(x)
    except ValueError:
        pass
            
    if x in [1,2,3]:
        print("x: ",x)
        return x
    else:
        main()


def generate_integer(level):
    x = random.randint((level - 1), (10**level - 1))
    y = random.randint((level - 1), (10**level - 1))
    return x, y


if __name__ == "__main__":
    main()