#!/usr/bin/env python3

import subprocess
import sys
import time
import RPi.GPIO as GPIO
import toml
from random import random
from simple_pid import PID
SLEEP_INTERVAL = 0.1


def get_temp():
    if config['control']['simulate']:
        temp = random()
    else:
        output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
        temp_str = output.stdout.decode()
        try:
            temp = float(temp_str.split('=')[1].split('\'')[0])
        except (IndexError, ValueError):
            raise RuntimeError('Could not parse temperature output')
    return temp


def stop():
    print('Exiting....')
    GPIO.cleanup()
    sys.exit()


def pid_control():
    try:
        while True:
            pv = get_temp()
            cv = pid(pv) * -1  # Invert cv to make a reverse acting loop
            pwm.ChangeDutyCycle(cv)
            time.sleep(SLEEP_INTERVAL)

    except KeyboardInterrupt:
        stop()


def on_off_control():
    try:
        while True:
            pv = get_temp()
            if pv >= config['control']['on_off']['on_temperature']:
                pass
            elif pv <= config['control']['on_off']['off_temperature']:
                pass
            time.sleep(SLEEP_INTERVAL)
    except KeyboardInterrupt:
        pwm.stop()
        stop()


if __name__ == '__main__':
    # Load configuration file
    config = toml.load('config.toml')

    mode = config['control']['mode']
    fan_pin = config['io']['fan_pin']

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fan_pin, GPIO.OUT)

    # PID mode setup
    if mode == 'pid':
        pwm = GPIO.PWM(fan_pin, config['io']['pwm_freq'])
        pwm.start(0)

        sample_time = config['control']['pid']['sample_time']
        pid = PID(Kp=config['control']['pid']['kp'],
                  Ki=config['control']['pid']['ki'],
                  Kd=config['control']['pid']['kd'],
                  setpoint=config['control']['pid']['setpoint'],
                  sample_time=config['control']['pid']['sample_time'],
                  output_limits=(-100, 0))

    # Kick off mode-dependent function
    if mode == 'on_off':
        on_off_control()
    elif mode == 'pid':
        pid_control()
