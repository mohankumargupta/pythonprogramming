from time import sleep
from PyMata.pymata import PyMata

COMPORT = 'COM13'
LEDPIN = 13
ANALOG_A0 = 0

uno = PyMata(COMPORT)
uno.set_pin_mode(LEDPIN,uno.OUTPUT, uno.DIGITAL)
print(dir(uno))
sleep(2)
uno.digital_write(LEDPIN,uno.HIGH)
sleep(2)
uno.digital_write(LEDPIN,uno.LOW)
sleep(2)
uno.enable_analog_reporting(ANALOG_A0)
sleep(2)
uno.get_analog_response_table()
sleep(2)
print(uno.analog_read(ANALOG_A0))
print(uno.get_firmata_version())
uno.close()