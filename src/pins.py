import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pins
FILL = 2
EMPTY = 3

# SECONDS TO SLEEP
SLEEP = 5

def output_fill():
    GPIO.setup(FILL, GPIO.OUT)

    GPIO.output(FILL, GPIO.HIGH)
    time.sleep(SLEEP)
    GPIO.output(FILL, GPIO.LOW)

    GPIO.cleanup()

def output_empty():
    GPIO.setup(EMPTY, GPIO.OUT)

    GPIO.output(EMPTY, GPIO.HIGH)
    time.sleep(SLEEP)
    GPIO.output(EMPTY, GPIO.LOW)

    GPIO.cleanup()
