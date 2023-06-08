import random
import pyfiglet
from art import *

ascii_banner = pyfiglet.figlet_format("Hello!!")
print(ascii_banner)
print("In this game of guess the number, there will be four levels. You will begin in level 1. To go to another level, you have to reach a certain amount of points.\n how to get points you get points when you finish the game but you want to finish the game quick because how many guesses you make less points you get ")

x = random.randint(1, 100)
count = 0
u = 20
points = 0

while True:
    y = int(input("Enter any number between 1 and 100: "))
    count += 1
    if x > y:
        print("Too Low!")
    elif x < y:
        print("Too Big!")
    elif x == y:
        text = "End"

        # Generate ASCII art for "End"
        end_art = text2art(text, font="block")

        # Generate ASCII art for the flowers
        flower_art = r"""
                (_\_)
              (_ <_{}
                (_/_)
              |\ |   
                \\| /|
                \|//
                  |/
            ,.,.,|.,.,.
            ^`^`^`^`^`^
        """

        # Combine the ASCII art for "End" with the flower art
        combined_art = flower_art + "\n" + end_art + "\n" + flower_art

        # Print the combined ASCII art
        print(combined_art)

        print("Hurray!")
        u = u - count
        points = points + u
        u = 20
        count = 0
        print("Your points are", points)
        t = str(input("Do you want to continue? Type Yes or No: "))
        if t == "no" or t == "No":
            break
        elif t == "yes" or t == "Yes":
            x = random.randint(1, 100)

    if points > 100:
        print("Congratulations, you achieved Level 2!")
        f = str(input("Do you want to go to Level 2? "))
        if f == "no" or f == "No":
            x = random.randint(1, 100)
        elif f == "yes" or f == "Yes":
            x = random.randint(1, 1000)
            while True:
                d = int(input("Enter a number between 1 and 1000: "))
                if x > d:
                    print("Too Low!")
                elif x < d:
                    print("Too Big!")
                elif x == d:
                    text = "End"

                    # Generate ASCII art for "End"
                    end_art = text2art(text, font="block")

                    # Generate ASCII art for the flowers
                    flower_art = r"""
                            (_\_)
                          (_ <_{}
                            (_/_)
                          |\ |   
                            \\| /|
                            \|//
                              |/
                        ,.,.,|.,.,.
                        ^`^`^`^`^`^
                    """

                    # Combine the ASCII art for "End" with the flower art
                    combined_art = flower_art + "\n" + end_art + "\n" + flower_art

                    # Print the combined ASCII art
                    print(combined_art)
                    print("Hurray!")
                    u = u - count
                    points = points + u
                    u = 20
                    count = 0
                    print("Your points are", points)
                    p = str(input("Do you want to continue? Type Yes or No: "))
                    if p == "no" or p == "No":
                        break
                    elif p == "yes" or p == "Yes":
                        x = random.randint(1, 1000)
                        if points > 300:
                            print("Congratulations, you achieved Level 3!")
                            fu = str(input("Do you want to go to Level 3? "))
                            if fu == "no" or fu == "No":
                                x = random.randint(1, 1000)
                            elif fu == "yes" or fu == "Yes":
                                x = random.randint(-10, 1000)
                                while True:
                                    do = int(input("Enter a number between -10 and 1000: "))
                                    if x > do:
                                        print("Too Low!")
                                    elif x < do:
                                        print("Too Big!")
                                    elif x == do:
                                        text = "End"

                                        # Generate ASCII art for "End"
                                        end_art = text2art(text, font="block")

                                        # Generate ASCII art for the flowers
                                        flower_art = r"""
                                                (_\_)
                                              (_ <_{}
                                                (_/_)
                                              |\ |   
                                                \\| /|
                                                \|//
                                                  |/
                                            ,.,.,|.,.,.
                                            ^`^`^`^`^`^
                                        """

                                        # Combine the ASCII art for "End" with the flower art
                                        combined_art = flower_art + "\n" + end_art + "\n" + flower_art

                                        # Print the combined ASCII art
                                        print(combined_art)
                                        print("Hurray!")
                                        u = u - count
                                        points = points + u
                                        u = 20
                                        count = 0
                                        print("Your points are", points)
                                        pw = str(input("Do you want to continue? Type Yes or No: "))
                                        if pw == "no" or pw == "No":
                                            break
                                        elif pw == "yes" or pw == "Yes":
                                            x = random.randint(-10, 1000)
                                            if points > 300:
                                                print("Congratulations, you achieved Level 4!")
                                                fu = str(input("Do you want to go to Level 4? "))
                                                if fu == "no" or fu == "No":
                                                    x = random.randint(-500, 1500)
                                                elif fu == "yes" or fu == "Yes":
                                                    x = random.randint(-500, 1500)
                                                    while True:
                                                        dwo = int(input("Enter a number between -500 and 1500: "))
                                                        if x > dwo:
                                                            print("Too Low!")
                                                        elif x < dwo:
                                                            print("Too Big!")
                                                        elif x == dwo:
                                                            text = "End"

                                                            # Generate ASCII art for "End"
                                                            end_art = text2art(text, font="block")

                                                            # Generate ASCII art for the flowers
                                                            flower_art = r"""
                                                                    (_\_)
                                                                  (_ <_{}
                                                                    (_/_)
                                                                  |\ |   
                                                                    \\| /|
                                                                    \|//
                                                                      |/
                                                                ,.,.,|.,.,.
                                                                ^`^`^`^`^`^
                                                            """

                                                            # Combine the ASCII art for "End" with the flower art
                                                            combined_art = flower_art + "\n" + end_art + "\n" + flower_art

                                                            # Print the combined ASCII art
                                                            print(combined_art)
                                                            print("Hurray!")
                                                            u = u - count
                                                            points = points + u
                                                            u = 20
                                                            count = 0
                                                            print("Your points are", points)
                                                            pww = str(input("Do you want to continue? Type Yes or No: "))
                                                            if pww == "no" or pww == "No":
                                                                break
                                                            elif pww == "yes" or pww == "Yes":
                                                                x = random.randint(-500, 1500)