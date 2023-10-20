from timer import stopwatch
from scoreboard import write_score_input
import time
import random

#Prints game mode options
def game_mode_print():
  print("Game mode select:")
  print("1. Classic")
  print("  Press the enter key at 10 seconds")
  print("2. Random")
  print("  Press the enter key at the number provided")
  print("")

#Asks users for their game mode choice
def game_mode_select():
  choice = input("Select a menu option or press enter to go back: ")
  if (choice == "1"):
    classic_mode()
  elif (choice == "2"):
    random_mode()
  elif (choice == ""):
    from boot_up import menu_sequence
    menu_sequence()
  else:
    print("Invalid choice; try again")
    game_mode_select()

#Prints menu and asks for input; used in other files
def game_mode_sequence():
  game_mode_print()
  game_mode_select()

#Starts 3 sec countdown before starting timer
def start_countdown():
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  print("\033c", end='')
  print("Timer started: waiting for input...")

#Prompts user if they want to store their score or return to menu
def end_round(score, game_mode):
  from boot_up import menu_sequence
  choice = input("Save score? (y/n): ")
  if (choice == "y"):
    write_score_input(score, game_mode)
    menu_sequence()
  elif (choice == "n"):
    menu_sequence()
  else:
    print("Invalid choice; try again")
    end_round(score, game_mode)

#Sees how close you are to the goal time
def calculate_score(goal, time):
  score = goal - time
  
  if (score < 0):
    score = score * -1
    return score
  else:
    return score

#Game modes

def classic_mode():
  print("\033c", end='')
  print("Blind mode selected")
  print("")
  print("Press the enter key at 10 seconds")
  start_countdown()
  time = stopwatch()
  print("You stopped the timer at ", time)
  print("You were within ", 10 - time, " seconds!")
  end_round(calculate_score(10, time), "classic")

def random_mode():
  print("\033c", end='')
  goal = random.randrange(1, 10)
  print("Random mode selected")
  print("")
  print("Press the enter key at ", goal, " seconds")
  start_countdown()
  time = stopwatch()
  print("You stopped the timer at ", time)
  print("You were within ", calculate_score(goal, time), " seconds!")
  end_round(calculate_score(goal, time), "blind")
