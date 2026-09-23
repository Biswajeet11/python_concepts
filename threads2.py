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

  t1 = threading.Thread(target = doSomething, args=["biswa"])
  t2 = threading.Thread(target = doSomething, args=["ravi"])

  t1.start()
  t2.start()

  t1.join()
  t2.join()
  
  finish = time.pref_counter() 
  print(f"\nFinished in {round(finish-start,2)}")
