import time
import random

game_mode = input("Enter game mode: P-ost = remember it backwards/M-emento = remember: ")

while True:
    game_char = input("Enter game characters: E-azy/N-ormal/H-ared: ")
    if game_char == "E":
        game_char = 6
        print("6 Characters")
        break
    elif game_char == "N":
        game_char = 12
        print("12 Characters")
        break
    elif game_char == "H":
        game_char = 15
        print("15 Characters")
        break
    else:
        continue

def gen():
    numb = ""
    for x in range(game_char):
      numb += str(random.randint(0, 9))
    return numb

while True:
    if game_mode == "M":
        numb = gen()
        print(numb)
        time.sleep(4)
        for x in range(256):
            print()
        if numb == input("Enter the number: "):
            print("Correct!")
        else:
            print("Fault...")
        print(numb)
        input("Press a key to continue...")
    elif game_mode == "P":
        numb = gen()
        print(numb)
        time.sleep(4)
        for x in range(256):
            print()
        numb = reversed(numb)
        if numb == input("Enter the number: "):
            print("Correct!")
        else:
            print("Fault...")
        print(numb)
        input("Press a key to continue...")