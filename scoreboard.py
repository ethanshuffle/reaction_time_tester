def scoreboard_menu_print():
  print("Scoreboards:")
  print("1. Classic Mode")
  print("2. Random Mode")
  print("3. Blind Mode")
  print("4. Return to Main Menu")
  print("")

def scoboard_menu_input():
  choice = input("Select a menu option: ")
  if (choice == "1"):
    get_scoreboard("classic")
  elif (choice == "2"):
    get_scoreboard("random")
  elif (choice == "3"):
    get_scoreboard("blind")
  elif (choice == "4"):
    from boot_up import menu_sequence
    menu_sequence()
  else:
    print("Invalid choice; try again")
    scoboard_menu_input()

def scoreboard_menu_sequence():
  scoreboard_menu_print()
  scoboard_menu_input()

def get_scoreboard(game_mode):
  file = open(game_mode + "_board.txt", "r")
  scores = file.readlines()
  file.close()
  print("\033c", end='')
  print_scoreboard(scores, game_mode)
  scoreboard_exit()

def scoreboard_exit():
  from boot_up import clear_console
  from boot_up import menu_sequence
  choice = input("Press enter to return to menu")
  if (choice == ""):
    clear_console()
    menu_sequence()
  else:
    clear_console()
    menu_sequence()

def print_scoreboard(scores, game_mode):
  print (game_mode.upper() + " SCOREBOARD:")
  print("")
  for i in range(10):
    split = scores[i].split(":")
    print(split[0].upper() + " : " + split[1])

def write_score_input(score, game_mode):
  name = input("Enter a 3 character name(ex. ECS): ")
  if (len(name) > 3 or len(name) < 3):
    print("Name not 3 characters, try again.")
    write_score_input(score, game_mode)
  else:
    insert = name + ":" + str(score) + "\n"
    file = open(game_mode + "_board.txt", "r")
    scores = file.readlines()
    file.close()
    for i in range(len(scores)):
      split = split = scores[i].split(":")
      if (score > float(split[1])):
        continue
      else:
        scores.insert(i, insert)
        file = open(game_mode + "_board.txt", "w")
        file.writelines(scores)
        file.close()
        break

