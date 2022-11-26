from itertools import cycle
import sys
from time import time, sleep

text = "Please note that attractions/activities may be closed or suspended at any time. Check official sites before visiting."

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \

STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    spinner = cycle(SPINNER_STATES)
    end = time() + seconds
    while time() < end:
        spin = next(spinner)
        sys.stdout.write('\r'+spin)
        sys.stdout.flush()
        sleep(STATE_TRANSITION_TIME)
    print()

if __name__ == '__main__':
    spinner(2)
