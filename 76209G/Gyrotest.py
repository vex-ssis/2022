#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
gyro_a = Gyro(brain.three_wire_port.a)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


#endregion VEXcode Generated Robot Configuration
vexcode_brain_precision = 0
vexcode_console_precision = 0
counter = 0

def main():
    global myVariable, counter, vexcode_brain_precision, vexcode_console_precision
    brain.screen.print("Calibrate Gyro:")
    gyro_a.calibrate()
    while gyro_a.is_calibrating():
        sleep(50)
    brain.screen.next_row()
    brain.screen.print("Done!")
    while True:
        brain.screen.set_cursor(4, 1)
        brain.screen.print("My current orientation is ")
        brain.screen.print(gyro_a.heading(DEGREES), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
        brain.screen.print(" degrees.    ")
        brain.screen.next_row()
        brain.screen.print("My current rotation is ")
        brain.screen.print(gyro_a.rotation(DEGREES), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
        brain.screen.print(" degrees.    ")
        brain.screen.next_row()
        brain.screen.print(counter, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
        brain.screen.print(". ")
        counter = counter + 1
        wait(0.1, SECONDS)
        wait(5, MSEC)

main()
