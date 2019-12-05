#!/usr/bin/env python3

import subprocess
import sys
import time
import RPi.GPIO as GPIO
import toml
from simple_pid import PID

SLEEP_INTERVAL = 0.1


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

    fan_pin = config['io']['fan_pin']
    pwm_freq = config['io']['pwm_freq']

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fan_pin, GPIO.OUT)
    pwm = GPIO.PWM(fan_pin, pwm_freq)
    pwm.start()

    kp = config['pid']['kp']
    ki = config['pid']['ki']
    kd = config['pid']['kd']
    sp = config['pid']['setpoint']
    sample_time = config['pid']['sample_time']
    pid = PID(Kp=kp, Ki=ki, Kd=kd, setpoint=sp, sample_time=sample_time)

    try:
        while True:
            pv = get_temp()
            cv = pid(pv)
            pwm.ChangeDutyCycle(cv)

            time.sleep(SLEEP_INTERVAL)

    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
        sys.exit()
