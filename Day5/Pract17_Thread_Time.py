import time
from tracemalloc import start
start = time.perf_counter()

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} completed")
    
    
task("Task1")
task("Task2")   
task("Task3")
############### total execution time - 6 secs
end = time.perf_counter()

print(f"Total time : {end - start:.2f} secs")
    
