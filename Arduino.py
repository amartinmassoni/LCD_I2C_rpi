#!/usr/bin/python3

"""Arduino constants and functions, copied from Arduino.h"""

from time import sleep

#define HIGH 0x1
HIGH = 0x1
#define LOW  0x0
LOW = 0x0

#define INPUT 0x0
INPUT = 0x0
#define OUTPUT 0x1
OUTPUT = 0x1
#define INPUT_PULLUP 0x2
INPUT_PULLUP = 0x2

def delay( ms ):
	sleep( ms / 1000 )

def delayMicroseconds( us ):
	sleep( ms / 1000000 )
