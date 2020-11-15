from abc import ABC, abstractmethod
import logging
import random
import time
import asyncio
from threading import Thread
import sys

class Plane:
  def __init__(self, roll_orientation, pitch_orientation, yaw_orientation, rate_of_correction):
    self.roll = roll_orientation
    self.pitch = pitch_orientation
    self.yaw = yaw_orientation
    self.autopilot = Correction(rate_of_correction)
  
  def get_position(self):
    logging.info("Current position is: Roll {:.2f} Pitch {:.2f} Yaw {:.2f}".format(self.roll, self.pitch, self.yaw))
  
  def correct_position(self):
    self.autopilot.apply_event(self)

class Event(ABC):
  @abstractmethod
  def apply_event(self):
    pass

class Environment(Event):

  def __init__(self, plane: Plane):
    self.plane = plane

  def apply_event(self):
    self.plane.roll += random.gauss(0,4)
    self.plane.pitch += random.gauss(0,4)
    self.plane.yaw += random.gauss(0,4)

class Correction(Event):

    def __init__(self, rate_of_correction):
      self.rate_of_correction = rate_of_correction
      
    def apply_event(self, plane: Plane ):
      if (plane.roll ) != 0 or (plane.pitch) != 0 or (plane.yaw) != 0:
        plane.roll += random.gauss(0, 2*self.rate_of_correction) if plane.roll < 0 else - random.gauss(0, 2*self.rate_of_correction)
        plane.pitch += random.gauss(0, 2*self.rate_of_correction) if plane.pitch < 0 else - random.gauss(0, 2*self.rate_of_correction)
        plane.yaw += random.gauss(0, 2*self.rate_of_correction) if plane.yaw < 0 else - random.gauss(0, 2*self.rate_of_correction)
      else:
        logging.info("No need to correct")

def flight():
  airbus = Plane(0,0,0, rate_of_correction=2.0)
  bermuda = Environment(airbus)

  logging.info("Welcome on the board of our plane, we wish you a pleasant flight!")
  logging.info("...")
  logging.info("Holy Moly, unexpected turbulence, hang in there!")
  global continue_loop
  while continue_loop:
    bermuda.apply_event()
    airbus.correct_position()
    airbus.get_position()
    time.sleep(1)

def get_input():
  logging.info("Press enter to stop the program")
  input()
  global continue_loop
  continue_loop = False

if __name__ == "__main__":
  
  logging.basicConfig(level=logging.INFO, format='%(message)s')
  continue_loop = True
  t1 = Thread(target = get_input)
  t2 = Thread(target = flight)
  t1.start()
  t2.start()
  t1.join()