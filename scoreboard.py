#Prints menu option
def scoreboard_menu_print():
  print("Scoreboards:")
  print("")
  print("1. Classic Mode")
  print("2. Random Mode")
  print("")

#Prompts user for input on which scoreboard they wish to view
def scoboard_menu_input():
  choice = input("Select a menu option or press enter to go back: ")
  if (choice == "1"):
    get_scoreboard("classic")
  elif (choice == "2"):
    get_scoreboard("random")
  elif (choice == ""):
    #This is in a couple of places; work around for circular import
    from boot_up import clear_console
    from boot_up import menu_sequence
    menu_sequence()
  else:
    print("Invalid choice; try again")
    scoboard_menu_input()

#Full scoreboard sequence, used in other calls
def scoreboard_menu_sequence():
  scoreboard_menu_print()
  scoboard_menu_input()

#Gets scoreboard for printing
def get_scoreboard(game_mode):
  #Opens file and stores each unprocessed line in an array
  file = open(game_mode + "_board.txt", "r")
  scores = file.readlines()
  file.close()

  #Clears console so we have a blank slate for printing
  print("\033c", end='')
  
  print_scoreboard(scores, game_mode)
  scoreboard_exit()

#Goes through array of scores, formats them, and prints them
def print_scoreboard(scores, game_mode):
  print (game_mode.upper() + " SCOREBOARD:")
  print("")
  for i in range(10):
    split = scores[i].split(":")
    print(split[0].upper() + " : " + "%.2f" % float(split[1]))

#Allows user to return to main menu
def scoreboard_exit():
  from boot_up import clear_console
  from boot_up import menu_sequence
  print("")
  
  choice = input("Press enter to return to menu")
  if (choice == ""):
    clear_console()
    menu_sequence()
  else:
    clear_console()
    menu_sequence()

#Writes score into text files
def write_score_input(score, game_mode):
  name = input("Enter a 3 character name(ex. ECS): ")
  #Verifies name is 3 characters
  if (len(name) > 3 or len(name) < 3):
    print("Name not 3 characters, try again.")
    write_score_input(score, game_mode)
  else:
    #Adds : between name and score
    insert = name + ":" + str(score) + "\n"
    file = open(game_mode + "_board.txt", "r")
    scores = file.readlines()
    file.close()
    #Checks where in the highscores the score goes
    for i in range(len(scores)):
      split = split = scores[i].split(":")
      if (score > float(split[1])):
        continue
      else:
        scores.insert(i, insert)
        file = open(game_mode + "_board.txt", "r+")
        data = file.read()
        file.seek(0)
        file.writelines(scores)
        file.truncate()
        file.close()
        break