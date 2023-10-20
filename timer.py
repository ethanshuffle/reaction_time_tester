import time

#Determines how much time has passed since the program started
#Time stops when enter is pressed
def stopwatch():

  starttime = time.time()
  value = "1"
  totaltime = ""

  while value.lower() != "":
    
    value = input()

    totaltime = round((time.time() - starttime), 2)
    
  return totaltime

#Would need to implement multithreading; not today lol
def visible_stopwatch(value):
  seconds = 0
  value = input()
  while value.lower() != "":
    for i in range(100000000000000000000000000000):
      seconds += 0.01
      print("Timer started: waiting for input...")
      print("")
      print("%.2f" % seconds)
      time.sleep(0.01)
      print("\033c", end='')
    break

