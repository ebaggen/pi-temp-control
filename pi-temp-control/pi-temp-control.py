#!/usr/bin/env python3

import subprocess
import time
import RPi.GPIO as GPIO
import toml
from simple_pid import PID

ON_THRESHOLD = 45
OFF_THRESHOLD = 40
SLEEP_INTERVAL = 1
GPIO_PIN = 18


def get_temp():
    output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
    temp_str = output.stdout.decode()
    try:
        return float(temp_str.split('=')[1].split('\'')[0])
    except (IndexError, ValueError):
        raise RuntimeError('Could not parse temperature output')


if __name__ == '__main__':
    # Load configuration file
    config = toml.load('config.toml')

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    pwm = GPIO.PWM(GPIO_PIN, 1000)
    pwm.start()

    pid = PID(setpoint=50)
    pid.sample_time = 0.1  # update every 0.1 seconds

    try:
        while True:
            # Basic switching implementation
            '''
            temp = get_temp()
            if temp > ON_THRESHOLD:
                GPIO.output(GPIO_PIN, GPIO.HIGH)
            elif temp < OFF_THRESHOLD:
                GPIO.output(GPIO_PIN, GPIO.LOW)
            '''

            # PID implementation
            pv = get_temp()
            cv = pid(pv)
            pwm.ChangeDutyCycle(cv)

            time.sleep(SLEEP_INTERVAL)

    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
        print("exit")
