# Team 76209G - Gravitational wave

## Team members - Winners of "Tipping Point" 2022 at SSIS

Our team consists of Tina (team captain), Milly, Meherika and Bomin. Our team color is red.

![Team G](../docs/76209G.jpeg)

## Robot: Gipsy Danger

![Robot 76209G](../docs/76209G_.jpeg)

## Code - the only autonomous points in 2022!

Last edit: June 3rd, 2022

``` py
myVariable = 0
counter = 0

def default():
    global myVariable, counter
    motor_group_4.set_velocity(180, PERCENT)
    drivetrain.set_drive_velocity(80, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)

def when_started1():
    global myVariable, counter
    default()
    motor_group_4.spin_for(REVERSE, 3100, DEGREES, wait=True)
    drivetrain.turn_for(RIGHT, 19, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 1280, MM, wait=True)
    motor_group_4.spin_for(FORWARD, 1450, DEGREES, wait=True)
    drivetrain.turn_for(RIGHT, 100, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 1500, MM, wait=True)
    drivetrain.drive_for(REVERSE, 500, MM, wait=True)
    drivetrain.turn_for(RIGHT, 40, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 900, MM, wait=True)
    motor_group_4.spin_for(REVERSE, 1400, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 500, MM, wait=True)

# Calibrate the Drivetrain
calibrate_drivetrain()

when_started1()

```
