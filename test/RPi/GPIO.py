BCM   = 'bcm'
BOARD = 'board'
IN    = 'in'
OUT   = 'out'

gpio_mode = BOARD
pins = [None]*20

def setmode(m):
    gpio_mode = m

def setup(pin, dir):
    pins[pin] = dir

def cleanup():
    pins = [None]*20

def output(pin, on):
    if pins[pin] == OUT:
        pass    # okay
    else:
        raise "pin %d not setup for output" % pin
    


