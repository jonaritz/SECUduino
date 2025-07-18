#! /usr/bin/env python3

"""Simple acquisition script for the Fast_Acquisition example.

This utility reads one byte from ``/dev/ttyUSB0`` at 1 Mbit/s, converts the
value to millivolts and prints the result.  The original version was written
for Python 2 and failed under Python 3 due to the ``print`` statement and the
behaviour of ``serial.read``.
"""

import serial
import sys


ser = serial.Serial("/dev/ttyUSB0", 1000000)
while True:
    try:
        n = ser.read()
        if not n:
            continue
        n = n[0] * 5000 / 255  # Convierto en mV
        print(n)
    except KeyboardInterrupt:
        ser.close()
        sys.exit(0)



