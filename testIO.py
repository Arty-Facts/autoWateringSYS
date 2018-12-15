from gpiozero import LED, Button
from time import sleep
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mode", type=int,
                            help="display a square of a given number")
args = parser.parse_args()
led = LED(17)
button = Button(2)
if args.mode == 1:
    while True:
        if button.is_pressed:
            led.off()
        else:
            led.on()
        sleep(1)
elif args.mode == 2:
    while True:
        led.on()
        sleep(5)
        led.off()
        sleep(3)


