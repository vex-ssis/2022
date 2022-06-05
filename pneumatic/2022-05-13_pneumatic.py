from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
digital_out_c = DigitalOut(brain.three_wire_port.c)

# wait for rotation sensor to fully initialize
wait(30, MSEC)

#endregion VEXcode Generated Robot Configuration
vexcode_brain_precision = 0
vexcode_console_precision = 0

myVariable = 0

def main():
    global myVariable, vexcode_brain_precision, vexcode_console_precision
    brain.screen.print("Start in 2 seconds")
    brain.screen.next_row()
    wait(2, SECONDS)
    digital_out_c.set(False)
    brain.screen.print("Open in 2 seconds.")
    brain.screen.next_row()
    wait(2, SECONDS)
    brain.screen.print("Open!")
    brain.screen.next_row()
    digital_out_c.set(True)
    wait(2, SECONDS)
    digital_out_c.set(False)
    brain.screen.print("And done")
    wait(2, SECONDS)
    # stop project not currently supported

main()