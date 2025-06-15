import os
import random
import time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import pygame

#Initiate the mixer and add sounds for the game
pygame.mixer.init()
sound_spin = pygame.mixer.Sound("Sounds/spin.mp3")
sound_win = pygame.mixer.Sound("Sounds/win.mp3")
sound_lose = pygame.mixer.Sound("Sounds/lose.mp3")
sound_freespin = pygame.mixer.Sound("Sounds/freespin.wav")
sound_jackpot = pygame.mixer.Sound("Sounds/jackpot.mp3")
sound_final = pygame.mixer.Sound("Sounds/final.mp3")


# Emojis for the game
cherries = "\U0001F352"
heart = "\u2764\uFE0F"
bell = "\U0001F514"
jackpot = "\U0001F3B0"
banana = "\U0001F34C"
watermelon = "\U0001F349"
lemon = "\U0001F34B"

#List of the symbols in the slots
symbols = [cherries, heart, bell, jackpot, banana, watermelon, lemon]

#Method to generate the slot row and print the above it design
def spin():
    print("Spinning....", flush = True)
    sound_spin.play()
    time.sleep(2)
    print("*****************************", flush = True)
    print(flush = True)
    return [random.choice(symbols) for _ in range(3)]

#Method to print the rows in the slots and the below design
def print_result(row):
    for symbol in row:
        time.sleep(0.5)
        print(symbol, end=" | ", flush=True)
    print()
    print()
    print("*****************************")
    print()

#Method to check if a prize is won and calculate it
def payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == watermelon:
            return bet * 2
        elif row[0] == lemon:
            return bet * 3
        elif row[0] == banana:
            return bet * 5
        elif row[0] == cherries:
            return bet * 10
        elif row[0] == heart:
            return bet * 15
        elif row[0] == bell:
            return bet * 20
        elif row[0] == jackpot:
            sound_jackpot.play()
            return bet * 100
    return 0

#Method to check for free spins
def free_spins(row):
    if row[0] == row[1] == row[2]:
        if row[0] == watermelon:
            return 2
        elif row[0] == lemon:
            return 3
        elif row[0] == banana:
            return 4
        elif row[0] == cherries:
            return 5
        elif row[0] == heart:
            return 8
        elif row[0] == bell:
            return 10
        elif row[0] == jackpot:
            return 20
    elif (row[0] == row[1]) or (row[1] == row[2]) or (row[0] == row[2]):
        return 1
    return 0

#Method to print a legend of the rewards from the combinations of symbols
def print_legend():
    print("*****************************")
    print("Prizes for 3 of anything: ")
    print(f"{watermelon}: 2 * bet and 2 free spins")
    print(f"{lemon}: 3 * bet and 3 free spins")
    print(f"{banana}: 5 * bet and 4 free spins")
    print(f"{cherries}: 10 * bet and 5 free spins")
    print(f"{heart}: 15 * bet and 8 free spins")
    print(f"{bell}: 20 * bet and 10 free spins")
    print(f"{jackpot}: 100 * bet and 20 free spins")
    print()
    print("*****************************")

#Method to print the user's history of spins
def print_history(history):
    for i, entry in enumerate(history[-5:], start = 1):
        symbols, win, prize = entry
        print(f"{i}. {' | '.join(symbols)}:  {'WIN' if win else 'LOSE'}  -> {'$' + str(prize) + "0" if win else '$0.00'}")
        print()
        print("*****************************")
        print()

#Method to display the user's current balance
def show_balance(balance):
    print(f"Your new balance is: ${balance:.2f}",flush = True)

#Method to check if the user has given a positive input
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Enter a valid number.")

#Method to check if the user has given a non negative input
def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Enter a valid number.")

#Method to display the main menu
def welcome_menu():
    while True:
        print("*****************************")            
        print("-----Welcome to Slots!!!-----")
        print(f"{cherries * 3}-{heart * 3}-{bell * 3}-{jackpot * 4}-{banana * 3}-{watermelon * 3}-{lemon * 3}")
        print("*****************************")
        print("Press R to see the rules and prizes!")
        print("Press S to start a new game!")
        print("Press Q to exit the game!")
        choice = input("Enter an input here: ").upper()
        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == "R":
            show_rules()
        elif choice == "S":
            start_game()
        elif choice == "Q":
            print("Exiting the game")
            time.sleep(1)
            print(f"Hope to see you soon again {heart}")
            sys.exit()
        else:
            print("*****************************")
            print("This is not a valid option!!!")
            print("*****************************")
        
#Method to display the rules menu
def show_rules():
    while True:
        print("*****************************")
        print("--Rules for the game/prizes--")
        print("*****************************")
        time.sleep(1.5)
        print("1. The slots will generate a row of 3 symbols", flush=True)
        time.sleep(1.5)
        print("2. Rewards are given only if all 3 symbols match", flush=True)
        time.sleep(1.5)
        print("3. The rewards are: ", flush=True)
        time.sleep(1)
        print(f"- For 3 {watermelon}, you receive bet * 2", flush=True)
        time.sleep(1)
        print(f"- For 3 {lemon}, you receive bet * 3", flush=True)
        time.sleep(1)
        print(f"- For 3 {banana}, you receive bet * 5", flush=True)
        time.sleep(1)
        print(f"- For 3 {cherries}, you receive bet * 10", flush=True)
        time.sleep(1)
        print(f"- For 3 {heart}, you receive bet * 15", flush=True)
        time.sleep(1)
        print(f"- For 3 {bell}, you receive bet * 20", flush=True)
        time.sleep(1)
        print(f"- For 3 {jackpot}, you receive bet * 100 (Grand Jackpot!)", flush=True)
        time.sleep(2)
        print("4. You choose how many spins to play in one go", flush=True)
        time.sleep(1.5)
        print("5. You can get free spins if you happen to get: ", flush=True)
        time.sleep(1)
        print(f"- For 3 {watermelon}, you receive 2", flush=True)
        time.sleep(1)
        print(f"- For 3 {lemon}, you receive 3", flush=True)
        time.sleep(1)
        print(f"- For 3 {banana}, you receive 4", flush=True)
        time.sleep(1)
        print(f"- For 3 {cherries}, you receive 5", flush=True)
        time.sleep(1)
        print(f"- For 3 {heart}, you receive 8", flush=True)
        time.sleep(1)
        print(f"- For 3 {bell}, you receive 10", flush=True)
        time.sleep(1)
        print(f"- For 3 {jackpot}, you receive 20", flush=True)
        time.sleep(1)
        print("-For 2 of the same symbols, you receive 1 ", flush=True)
        time.sleep(2)
        print("6. You enter the game with a balance of your choice", flush=True)
        time.sleep(1.5)
        print("7. You can withdraw any time", flush=True)
        time.sleep(1.5)
        print("8. If your balance goes to 0, even if you get a free spin, it will not matter - game ends", flush = True)
        time.sleep(2)
        print("*****************************", flush=True)
        print("Press W to go to the welcome menu")
        print("Press S to start a new game!")
        print("Press Q to exit the game!")
        choice = input("Enter an input here: ").upper()
        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == "W":
            return
        elif choice == "S":
            start_game()
            return
        elif choice == "Q":
            print("Exiting the game")
            time.sleep(1)
            print(f"Hope to see you soon again {heart}")
            sys.exit()
        else:
            print("*****************************")
            print("This is not a valid option!!!")
            print("*****************************")

#List to store the user's previous spins
history = []

def start_game():
    print("*****************************")
    print()
    print("-----Welcome to the game-----")
    print(f"     {jackpot * 9} " )
    print()
    print("*****************************")
    print()
    balance = get_positive_float("Enter your balance: ")        #asking for the user's balance
    print("Entering your balance: ", end="")
    for _ in range(3):
        print(".", end=" ", flush=True)
        time.sleep(1)
    print()
    print(f"Thank you! Your balance for the game is ${balance:.2f}")
    print(flush = True)
    time.sleep(2)
    print("*****************************",flush = True)
    print(f"{cherries * 5}  Good luck! {cherries * 5}")
    print("*****************************")

    while True:
        bet = get_positive_float("Enter a bet: ")          #asking the user for their bet

        if bet > balance:                                    #checking whether this bet is bigger than the balance of the user
            print(f"A bet cannot be bigger than your balance - ${balance:.2f}")
            continue

        spins = get_non_negative_int("Enter a number of spins: ")      #asking the user for number of spins

        if spins == 0:                                                 #check
            print("You chose 0 spins. Returning to main menu.")
            return
      
        if spins * bet > balance:                                      #checking for overall bet = vet * spins to be less than the balance
            print("You do not have enough balance for that many spins.")
            continue

        os.system('cls' if os.name == 'nt' else 'clear')            #printing the legend for the spinning 
        print_legend()
        print()
        print("-----------------------------")
        print()
        
        while spins > 0:                                           #spin state
            balance -= bet                                  #decreasing the balance
            row = spin()
            print_result(row)
            time.sleep(1)

            prize = payout(row, bet)                     #check if the user has won
            win = prize > 0                              #boolean variable to check whether the user has won or not
            history.append((row, win, prize))            #adding the spin to the history list
            max_history = 5                              #limiting the size of the history list
            size_history = len(history) 
            if size_history > max_history:               #removing elements from the history of needed
                history.pop(0)
            extra_spins = free_spins(row)

            if extra_spins > 0:                         #checking whether the user got any extra spins
                time.sleep(0.5)
                print(f"You earned {extra_spins} free spin{'s' if extra_spins > 1 else ''}!", flush = True)
                sound_freespin.play()
                spins += extra_spins
                
            if prize == 0:                              #User lost
                time.sleep(0.5)
                print("Sorry, you lost this round.", flush = True)
                time.sleep(0.5)
                show_balance(balance)
                sound_lose.play()

                if balance <= 0:                       #Game over check
                    time.sleep(0.5)
                    print("You are out of money!!!", flush=True)
                    sound_final.play()
                    time.sleep(1)
                    print("Returning you to the main menu...", flush=True)
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
            else:                                    #User won
                time.sleep(0.5)
                print(f"Congratulations!!! You won ${prize:.2f}", flush = True)
                time.sleep(0.5)
                balance += prize
                show_balance(balance)
                sound_win.play()

            spins-=1           
            print()

            print("Your history of spins: ", flush = True)       #printing the user's history of spins
            print("*****************************", flush = True)
            print()
            print_history(history)

        # Ask if they want to continue
        while True:
            choice = input("Press 1 to continue, 0 to stop: ")
            if choice == "1":
                break
            if choice == "0":
                print(f"\nYou have finished the game with a balance of: ${balance:.2f}")
                print("*****************************")
                print("Press W to go to the welcome menu")
                print("Press R to see the rules")
                print("Press S to start a new game!")
                print("Press Q to exit the game!")

                
                while True:
                    next_state = input("Enter your choice here: ").upper()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if next_state == "W":
                        return  # Go back to welcome menu
                    elif next_state == "R":
                        show_rules()
                        # After showing rules, show the options again
                        print("*****************************")
                        print("Press W to go to the welcome menu")
                        print("Press R to see the rules")
                        print("Press S to start a new game!")
                        print("Press Q to exit the game!")
                    elif next_state == "S":
                        start_game()
                        return
                    elif next_state == "Q":
                        print("Exiting the game")
                        time.sleep(1)
                        print(f"Hope to see you soon again {heart}")
                        sys.exit()
                    else:
                        print("*****************************")
                        print("This is not a valid option!!! Try again.")


def main():
    welcome_menu()

if __name__ == '__main__':
    main()
