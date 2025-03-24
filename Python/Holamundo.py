import random

def roll_d6():
    return random.randint(1, 6)

if __name__ == "__main__":
    result = roll_d6()
    print(f"You rolled a {result}")