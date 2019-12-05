#!/usr/bin/env python3

import subprocess
import time
import RPi.GPIO as GPIO

ON_THRESHOLD = 45
OFF_THRESHOLD = 40
SLEEP_INTERVAL = 1
GPIO_PIN = 17

def get_temp():
  output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
  temp_str = output.stdout.decode()
  try:
    return float(temp_str.split('=')[1].split('\'')[0])
  except (IndexError, ValueError):
    raise RuntimeError('Could not parse temperature output')


if __name__ == '__main__':
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(GPIO_PIN, GPIO.OUT)

  try:
    while True:
      temp = get_temp()
      if temp > ON_THRESHOLD:
        GPIO.output(GPIO_PIN, GPIO.HIGH)
      elif temp < OFF_THRESHOLD:
        GPIO.output(GPIO_PIN, GPIO.LOW)
      time.sleep(SLEEP_INTERVAL)

  except KeyboardInterrupt:
    GPIO.cleanup()
    print("exit")

