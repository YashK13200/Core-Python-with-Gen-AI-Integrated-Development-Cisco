# A Car has an Engine

class Engine:
   def start(self):
       print("Engine started")

class Car:
  def __init__(self):
      self.engine_obj = Engine() # has-a -> Car has-a Engine
  
  def driving(self):
      self.engine_obj.start()
      print("Car is driving")


obj = Car()
obj.driving()
