import time
import threading

start = time.pref_counter()

def doSomething():
  print("Doing something")
  time.sleep(1)
  print("Done something")
  



if __name__ == "__main__":

  print(f"Thread name is {threading.current_thread().name} with id -{threading.get_ident()}")

  t1 = threading.Thread(target = doSomething)
  t2 = threading.Thread(target = doSomething)

  t1.start()
  t2.start()

  t1.join()
  t2.join()
  
  finish = time.pref_counter() 
  print(f"\nFinished in {round(finish-start,2)}")
