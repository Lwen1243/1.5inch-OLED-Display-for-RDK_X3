import sys
import signal
import Hobot.GPIO as GPIO
import time 

def signal_handler(signal, frame):
    sys.exit(0)

output_pin = 33

GPIO.setwarnings(False)

def main():
    GPIO.setmode(GPIO.BOARD)
    p = GPIO.PWM(output_pin, 48000)

    val = 50
    p.ChangeDutyCycle(val)
    p.start(val)
    try:
        while True:
            p.ChangeDutyCycle(val)
    finally:
        p.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()

    


