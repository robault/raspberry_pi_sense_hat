from sense_hat import SenseHat
from random import randint
from time import sleep
import datetime

sense = SenseHat()
sense.clear()

color_group = 4
black_group = 6
delay = 0.1
runtime_seconds = 10
start = datetime.datetime.today()

def set_color():
  x = randint(0,7)
  y = randint(0,7)
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  sense.set_pixel(x, y, r, g, b)

def blackout():
  x = randint(0,7)
  y = randint(0,7)
  sense.set_pixel(x, y, 0, 0, 0)

def group_loop():
  j = 0
  k = 0
  while j <= black_group:
    blackout()
    j += 1
  while k <= color_group:
    set_color()
    k += 1

def main_loop():
  i = 0
  elapsed = 0
  while elapsed < runtime_seconds:
    group_loop()
    sleep(delay)
    i += 1
    now = datetime.datetime.today()
    new_elapsed = int((now - start).total_seconds())
    if int(elapsed) < int(new_elapsed):
      elapsed = new_elapsed
      print(elapsed,"of",runtime_seconds,"seconds")

print("Starting...")
main_loop()
sense.clear()
print("Finished.")