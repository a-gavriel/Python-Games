import requests
import re
import threading
import time
from datetime import datetime


thread_running = False
thread_var : threading.Thread
thread_result = False
viagogo_test_blacklist = False
timeout_time = 300
last_check_time = datetime.now()

class Page:
  def __init__(self, name, url, pattern, options):
    self.name = name
    self.url = url
    self.text = ""
    self.pattern = pattern
    self.pattern_options = options
    self.finds = []
    #self.get_text()

  def get_text(self):
    self.text = ((requests.get(self.url)).text).lower()

  def find(self):
    if self.pattern != "":
      if self.pattern_options == "":
        self.finds = re.findall(self.pattern, self.text)
      else:
        self.finds = re.findall(self.pattern, self.text, self.pattern_options)

  def filter_finds(self, pattern):
    if self.finds != []:
      for i, current in enumerate(self.finds):
        m = re.match(pattern, current)
        if m is not None:
          self.finds.pop(i)

  def __str__(self):
    return (
      f"""
      Name:\t{self.name}
      Url:\t{self.url[12:30]}...
      Pattern:\t{self.pattern}
      Finds:\t{self.finds}"""
    )

eticket = Page("eticket", "https://www.eticket.cr/eventos.aspx?categoria=1&", 
                  ".{1,10}mägo de oz.{5,10}|.{1,10}mago de oz.{1,10}|.{1,10}mago.{1,10}", "" )

viagogo =  Page("viagogo", "https://www.viagogo.com/ww/Concert-Tickets/Hard-Rock-Metal/Mago-De-Oz-Tickets", 
                  ".{1,30}costa rica.{1,30}", "" )

def check_pages():
  global viagogo_test_blacklist

  log = "Checking pages:\n"
  results = []
  try:
    eticket.get_text()
    viagogo.get_text()

    log += "\nChecking: eticket\t"
    eticket.find()
    if (eticket.finds == []):
      log += "None"
    else:
      log += f": {len(eticket.finds)} result(s)!"

    log += "\nChecking: viagogo\t"
    viagogo.find()
    
    if not viagogo_test_blacklist:
      viagogo.filter_finds(".*currency.*")


    if (viagogo.finds == []):
      log += "None"
    else:
      log += f": {len(viagogo.finds)} result(s)!"


    results.extend(eticket.finds)
    results.extend(viagogo.finds)

  except:
    log += "Error getting data"


  return(results, log)



def del_blacklist() -> str:
  """
  Test function to invert viagogo's  blacklist function

  """
  global viagogo_test_blacklist
  viagogo_test_blacklist = not viagogo_test_blacklist
  print(viagogo_test_blacklist)
  return str(viagogo_test_blacklist)



def thread_function(reply_function):
  """
  Checks every second if should exit, if not check every "timeout time" the webpages
  """
  global thread_result, thread_running, last_check_time
  thread_result = False
  while not thread_result:
    for i in range(timeout_time):
      time.sleep(1)
      if not thread_running:
        print("exiting")
        return 
    
    
    last_check_time = datetime.now()
    current_time = last_check_time.strftime("%H:%M:%S")
    print("Running Thread - " + current_time)

    result = check_pages()
    if result[0] != []:
      reply_function("RESULT FOUND!")
      reply_function(result[1])
      thread_result = True
      thread_running = False
      return
      
  
def change_timeout(message, reply_function) -> None:
  """
  Changes the timeout between requests to the different webpages
  """
  global timeout_time
  timeout_time = 300  
  try:
    message = message.split()[1]
    timeout_time = int(message)
    if timeout_time < 1:
      raise Exception("Not enough time")
    reply_function("Set timeout:" + str(timeout_time))
  except:
    reply_function("Set timeout:" + str(timeout_time))



def create_thread(reply_function) -> None:
  """
  Creates the thread that searches through the web pages
  """
  global thread_running, thread_var, last_check_time
  if thread_running:
    temp = last_check_time.strftime("%H:%M:%S")
    reply_function(f"Thread already running!, last check on {temp}")

  else:
    thread_running = True
    thread_var = threading.Thread(target=thread_function, args=(reply_function,))
    thread_var.start()
    

    
