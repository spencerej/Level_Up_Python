import random
import time


def waiting_game():
    

    

    number = random.randint(1,10)
    input(f"Your target time is {number} seconds ----Press ENTER to Begin----")
    start_time =  time.time()
    input(f"Press ENTER again after {number} seconds...")
    elapsed_time = time.time() - start_time

    print(f"Elapsed time: {elapsed_time} seconds")
    if elapsed_time == number:
        print("That is incredible! You were spot on!")
    elif elapsed_time > number:
        print(f"{elapsed_time - number} seconds too slow!")
    else:
        print(f"{number - elapsed_time} seconds too quick!")
    

