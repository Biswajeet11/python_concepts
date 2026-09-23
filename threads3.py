import time
import threading

start = time.pref_counter()

def doSomething(person_name):
  print("Doing something")
  time.sleep(1)
  print(person_name)
  print("Done something")
  



if __name__ == "__main__":

  print(f"Thread name is {threading.current_thread().name} with id -{threading.get_ident()}")

  names = ['Riya','Shyam', 'abhijeet']
 
  threads = []
  for  name in names:
    thread = threading.Thread(target = doSomething, args=[name])
    thread.start()
    threads.append(thread)

  for thread in threads:
    thread.join()
  
  finish = time.pref_counter() 
  print(f"\nFinished in {round(finish-start,2)}")
