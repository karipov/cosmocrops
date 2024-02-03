import RPi.GPIO as GPIO

if __name__ == "__main__":
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
