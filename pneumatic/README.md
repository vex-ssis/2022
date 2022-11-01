# Pneumatic in VEX

We have one set with a 100 psi pressure cylinder and 2 single-action pistons with feather for return. The system was tested at the end of May 2022.

You have to use one of the 3-pin connectors as digital output. We wrote [a program](https://github.com/vex-ssis/2022/blob/main/pneumatic/pneumatic3.v5python) that opens the valve for a second and closes it for a second and prints the counter on the display.

## Content of pneumatic3.v5python

This is in the file (the \n have been replaced):

``` py
{"mode":"Text","textContent":"#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
digital_out_c = DigitalOut(brain.three_wire_port.c)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


#endregion VEXcode Generated Robot Configuration

vexcode_console_precision = 0
myVariable = 0
cycles = 0

def when_started1():
    global myVariable, cycles, vexcode_brain_precision, vexcode_console_precision
    cycles = 1
    brain.screen.print(\"Start in 2 second\")
    brain.screen.next_row()
    digital_out_c.set(False)
    wait(2, SECONDS)
    while True:
        for repeat_count in range(10):
            brain.screen.print(\"Open for 1 sec, \")
            digital_out_c.set(True)
            wait(1, SECONDS)
            brain.screen.print(\"and closed for 1 sec. \")
            digital_out_c.set(False)
            brain.screen.print(cycles, precision=6)
            brain.screen.next_row()
            wait(1, SECONDS)
            cycles = cycles + 1
            wait(5, MSEC)
        brain.screen.set_cursor(1, 1)
        for repeat_count2 in range(11):
            brain.screen.print(\"                                                                 .\")
            brain.screen.next_row()
            wait(5, MSEC)
        brain.screen.set_cursor(1, 1)
        wait(5, MSEC)
    # stop project not currently supported

when_started1()
","textLanguage":"python","rconfig":[{"port":[3],"name":"digital_out_c","customName":false,"deviceType":"DigitalOut","deviceClass":"digital_out","setting":{},"triportSourcePort":22}],"slot":2,"platform":"V5","sdkVersion":"20220215.18.00.00","appVersion":"2.3.1","fileFormat":"1.0.1","icon":"","targetBrainGen":"First","target":"Physical"}
```
