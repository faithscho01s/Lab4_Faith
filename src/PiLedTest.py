import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

def init():
    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN) #set GPIO 22 as input
    GPIO.setup(24, GPIO.OUT)  # set GPIO 24 as output

def main():
    init()
    read_slide_switch()

def set_output(led, level):
    GPIO.output(24, level)

def read_slide_switch():
    ret = 0

    if GPIO.input(22):
        ret = 1
        set_output(24, 1)
        sleep(0.2)
        set_output(24, 0)
        sleep(0.2)

    else:
        ret = 0
        i = 0
        while i < 5:
            set_output(24, 1)
            sleep(0.1)
            set_output(24, 0)
            sleep(0.1)
            if i == 5:
                set_output(24, 0)
                break
            i += 1


    return ret


if __name__ == "__main__":
    while True:
        main()
