import time

def stopwatch():

  starttime = time.time()
  value = "1"
  totaltime = ""

  while value.lower() != "":
    
    value = input()

    totaltime = round((time.time() - starttime), 2)
    
  return totaltime