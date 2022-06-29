import time
import random

while True:
    game_mode = input("Enter diffeculty E-azy/N-ormal/H-ared")
    if game_mode == "E":
        game_mode = 6
        break
    elif game_mode == "N":
        game_mode = 12
        break
    elif game_mode == "H":
        game_mode = 15
        break
    else:
        continue

def gen():
    numb = ""
    for x in range(game_mode):
      numb += random.randInt(9+1)
    return numb

while True:
    numb = gen()
    print(numb)
    time.sleep(4)
    for x in range(256):
        print()
    if numb == input("Enter the number: "):
        print("Correct!")
    else:
        print("Fault...")