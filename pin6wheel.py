#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import signal
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

def exit_gracefully(signal, frame):
  GPIO.cleanup()
  sys.exit(0)
signal.signal(signal.SIGINT, exit_gracefully)

while True:
  GPIO.output(21, False)
  GPIO.output(19, False)
  GPIO.output(6, True)
  time.sleep(1)

  GPIO.output(21, False)
  GPIO.output(19, True)
  GPIO.output(6, False)
  time.sleep(1)

  GPIO.output(21, True)
  GPIO.output(19, False)
  GPIO.output(6, False)
  time.sleep(1)
