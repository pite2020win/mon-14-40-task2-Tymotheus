import random

def main():
  tilt = 0
  print("Welcome on the board of our plane, we wish you a pleasant flight!")
  print("...")
  print("Holy Moly, unexpected turbulence, hang in there!")
  while True:
    tilt = random.gauss(0,180)
    print("Current roll orientation is {:.2f} degrees.".format(tilt))
    print("Autopilot is correcting the orientation by {:.2f} degrees.".format(-tilt))
    tilt -= tilt
    print("Should we continue the flight? Type anything to proceed. Type 'no' to exit and teleport back home.")
    if input() == 'no':
      break

if __name__ == "__main__":
  main()
