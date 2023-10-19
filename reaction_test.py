from timer import stopwatch
from scoreboard import write_score_input
import time
import random

def game_mode_print():
  print("Game mode select:")
  print("1. Classic")
  print("  Press the enter key at 10 seconds")
  print("2. Random")
  print("  Press the enter key at the number provided")
  print("3. Blind")
  print("  No timer, all reflexes. Press enter at 10 seconds")
  print("")

def game_mode_select():
  choice = input("Select a menu option or press enter to go back: ")
  if (choice == "1"):
    classic_mode()
  elif (choice == "2"):
    random_mode()
  elif (choice == "3"):
    blind_mode()
  elif (choice == ""):
    from boot_up import menu_sequence
    menu_sequence()
  else:
    print("Invalid choice; try again")
    game_mode_select()

def game_mode_sequence():
  game_mode_print()
  game_mode_select()

def start_countdown():
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  print("\033c", end='')
  print("Timer started: waiting for input...")

def classic_mode():
  print("Classic mode is still under development, sorry!")
  game_mode_select()

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

def blind_mode():
  print("\033c", end='')
  print("Blind mode selected")
  print("")
  print("Press the enter key at 10 seconds")
  start_countdown()
  time = stopwatch()
  print("You stopped the timer at ", time)
  print("You were within ", 10 - time, " seconds!")
  end_round(calculate_score(10, time), "blind")

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
    
def calculate_score(goal, time):
  score = goal - time
  
  if (score < 0):
    score = score * -1
    return score
  else:
    return score