# Team 76209X

Until May the team liked to program in block code. But on May 24th they lost the `goto` function programmed and saved in block code. And had to rewrite the program. The file was saved as

## Blocks code

Taking this code and adding a few `LFCR` to it, together with some `TAB` it becomes readable. The goto function is indeed lost:

``` xml
{
"mode":"Blocks",
"workspace":"<xml xmlns=\"http://www.w3.org/1999/xhtml\">
<variables>
	<variable 
		type=\"\" 
		id=\"d?(~;^We:kZjpf`TwRSq\" 
		islocal=\"false\" 
		iscloud=\"false\" 
		arraylength=\"0\" 
		arraywidth=\"0\">x1
	</variable>
	<variable 	
		type=\"\" 
		id=\"3,?igH1K_s+v)(vfwq3l\" 
		islocal=\"false\" 
		iscloud=\"false\" 
		arraylength=\"0\" 
		arraywidth=\"0\">y1
	</variable>
</variables>

<block type=\"v5_events_when_started\" id=\".NsXwU_L.OuU1l7Sho$F\" deletable=\"false\" x=\"730\" y=\"-570\">
	<next>
	<block type=\"v5_variables_set_variable\" id=\"M3sZB,u$-Ha15)X~QPv_\">
		<field name=\"VARIABLE\" id=\"d?(~;^We:kZjpf`TwRSq\" variabletype=\"\">x1</field>
		<value name=\"VALUE\">
			<shadow type=\"math_number\" id=\"S-n$zF3a@+KiQy3{EIo_\">
				<field name=\"NUM\">-1400</field>
			</shadow>
		</value>
		<next>
		<block type=\"v5_variables_set_variable\" id=\"uxF]dbyihPHEp7KL!L}P\">
			<field name=\"VARIABLE\" id=\"3,?igH1K_s+v)(vfwq3l\" variabletype=\"\">y1</field>
			<value name=\"VALUE\">
				<shadow type=\"math_number\" id=\"n[@4Keirw;~NjAh=pRC#\">
					<field name=\"NUM\">1320</field>
				</shadow>
			</value>
			<next>	
			<block type=\"v5_sensing_calibrate_gyro\" id=\"M1GreP?|SFtH2bIC:N}6\">
				<field name=\"GYRO\">GyroA</field>
				<next>
				<block type=\"procedures_call\" id=\"4)l`1ahI|S_[x#7]4]{,\">
					<mutation 
						proccode=\"Goto %n x %n y\" 
						proceduredefid=\"dLr)pJCUCcAehw4|j?2a\" 
						argumentids=\"[&quot;V/m()E{96Jt(I6ykh=pX&quot;,&quot;Dn{kF`=CPnbCl(DDi+O8&quot;]\" 
						warp=\"false\">
					</mutation>
					<value name=\"V/m()E{96Jt(I6ykh=pX\">
						<shadow type=\"math_number\" id=\"+s:Y#G;U[Rp:TG3V=r=p\">
							<field name=\"NUM\">0</field>
						</shadow>
					</value>
					<value name=\"Dn{kF`=CPnbCl(DDi+O8\">
						<shadow type=\"math_number\" id=\"*Lvl$C,T*E@#F-snQ/!|\">
							<field name=\"NUM\">0</field>
						</shadow>
					</value>
					<next>
					<block type=\"procedures_call\" id=\"sCSABBTu!NGTkN_O;{fd\">
						<mutation 
							proccode=\"Goto %n x %n y\" 
							proceduredefid=\"dLr)pJCUCcAehw4|j?2a\" 
							argumentids=\"[&quot;V/m()E{96Jt(I6ykh=pX&quot;,&quot;Dn{kF`=CPnbCl(DDi+O8&quot;]\" 
							warp=\"false\">
						</mutation>
						<value name=\"V/m()E{96Jt(I6ykh=pX\">
							<shadow type=\"math_number\" id=\".J+9mt{q@ZM(|KxRX]$2\">
								<field name=\"NUM\">1000</field>
							</shadow>
						</value>
						<value name=\"Dn{kF`=CPnbCl(DDi+O8\">
							<shadow type=\"math_number\" id=\"V?d|dO0lLvAXHk]i4R~9\">
								<field name=\"NUM\"></field>
							</shadow>
						</value>
					</block>
					</next>
				</block>
				</next>
			</block>
			</next>
		</block>
		</next>
	</block>
	</next>
</block>
<block type=\"v5_events_when_controller_button\" id=\"T4`I;X7~qR{9SPQ6py%!\" x=\"730\" y=\"-190\">
	<field name=\"CONTROLLER\">Controller1</field>
	<field name=\"BUTTON\">ButtonR2</field>
	<field name=\"EVENTTYPE\">released</field>
	<next>
	<block type=\"v5_motion_stop_motor\" id=\"7!?UqU[#^gkFf(`N7+!Q\">
		<field name=\"MOTOR\">MotorGroup3</field>
	</block>
	</next>
</block>
<block type=\"v5_events_when_controller_button\" id=\"*i@/D#!2J!We;r.:YgjQ\" x=\"730\" y=\"50\">
	<field name=\"CONTROLLER\">Controller1</field>
	<field name=\"BUTTON\">ButtonR1</field>
	<field name=\"EVENTTYPE\">pressed</field>
	<next>
	<block type=\"v5_motion_spin\" id=\"mQL[n9M5XhS#vH{oa_5$\">
		<field name=\"MOTOR\">MotorGroup3</field>
		<field name=\"DIRECTION\">fwd</field>
	</block>
	</next>
</block>
</xml>",
"rconfig":
[
	{
		"port":[2,1,0],
		"name":"Drivetrain",
		"customName":false,
		"deviceType":"Drivetrain",
		"deviceClass":"smartdrive",
		"setting":{
			"type":"2-motor",
			"wheelSize":"wheel4in",
			"gear":"ratio18_1",
			"gearRatio":"1:1",
			"direction":"fwd",
			"gyroType":"none",
			"width":"295",
			"unit":"mm",
			"wheelbase":"40",
			"wheelbaseUnit":"mm",
			"xOffset":"0",
			"xOffsetUnit":"mm",
			"yOffset":"0",
			"yOffsetUnit":"mm",
			"thetaOffset":"180"
		}
	},
	{
		"port":[1],
		"name":"GyroA",
		"customName":false,
		"deviceType":"Gyro",
		"deviceClass":"gyro",
		"setting":{},
		"triportSourcePort":22
	},
	{
		"port":[],
		"name":"Controller1",
		"customName":false,
		"deviceType":"Controller",
		"deviceClass":"controller",
		"setting":{
			"left":"",
			"leftDir":"false",
			"right":"",
			"rightDir":"false",
			"upDown":"",
			"upDownDir":"false",
			"xB":"",
			"xBDir":"false",
			"drive":"tank",
			"id":"primary"
		}
	},
	{
		"port":[3,4],
		"name":"MotorGroup3",
		"customName":false,
		"deviceType":"MotorGroup",
		"deviceClass":"motor_group",
		"setting":{
			"fwd":"forward",
			"rev":"reverse",
			"gear":"ratio36_1",
			"motor_a_reversed":"false",
			"motor_b_reversed":"true"
		}
	}
],
"slot":0,
"platform":"V5",
"sdkVersion":"20220215.18.00.00",
"appVersion":"2.3.1",
"fileFormat":"1.0.1",
"icon":"",
"targetBrainGen":"First",
"cppStatus":"false",
"cpp":"//Invalid Graphical Code",
"target":"Physical"
}
```

Now compare the last part to the regular `v5python` code:

## v5 Python

``` py
{
"mode":"Text",
"textContent":"
#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_drive_smart = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
drivetrain_gyro = Gyro(brain.three_wire_port.a)
drivetrain = SmartDrive(left_drive_smart, right_drive_smart, drivetrain_gyro, 319.19, 320, 40, MM, 1)
controller_1 = Controller(PRIMARY)
fork_motor_group_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
fork_motor_group_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
fork_motor_group = MotorGroup(fork_motor_group_motor_a, fork_motor_group_motor_b)


# wait for rotation sensor to fully initialize
wait(30, MSEC)

def calibrate_drivetrain():
    # Calibrate the Drivetrain Gyro
    sleep(200, MSEC)
    brain.screen.print(\"Calibrating\")
    brain.screen.next_row()
    brain.screen.print(\"Gyro\")
    drivetrain_gyro.calibrate()
    while drivetrain_gyro.is_calibrating():
        sleep(25, MSEC)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

# define variables used for controlling motors based on controller inputs
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3
            # right = axis2
            drivetrain_left_side_speed = controller_1.axis3.position()
            drivetrain_right_side_speed = controller_1.axis2.position()
            
            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    left_drive_smart.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    right_drive_smart.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True
rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)



#endregion VEXcode Generated Robot Configuration

import math

def goto(target_x, target_y, reverse):
    #x1 = gps.x_position(MM)
    #y1 = gps.y_position(MM)
    delta_x = target_x - x1
    delta_y = target_y - y1
    distance = math.sqrt(delta_x**2 + delta_y**2)     # pythagorean theorem
    if ( delta_x == 0 ):
        if ( delta_y < 0):
            direction = 90
        else:
            direction = 270
    else:
        direction = - math.atan(delta_y / delta_x) * 180 / math.pi
    if ( delta_x < 0 ):
        direction = direction + 180
    if ( reverse != 0 ):
        direction = direction + 180
    if ( direction > 360 ):
        direction = direction - 360
    drivetrain.turn_to_heading(direction, DEGREES, wait=True)
    if ( reverse != 0 ):
        drivetrain.drive_for(REVERSE, distance, MM, wait=True)
    else:
        drivetrain.drive_for(FORWARD, distance, MM, wait=True)
def pick_up():
    fork_motor_group.spin_to_position(1500, DEGREES, wait=True)
def set_down():
    fork_motor_group.spin_to_position(1800, DEGREES, wait=True)

def when_started1():
    global myVariable, x1, y1
    x1 = -1400
    y1 = 1320
    goto(0, 0, 0)

# Calibrate the Drivetrain
calibrate_drivetrain()

when_started1()


",
"textLanguage":"python",
"rconfig":[
	{
		"port":[2,1,1],
		"name":"drivetrain",
		"customName":false,
		"deviceType":"Drivetrain",
		"deviceClass":"smartdrive",
		"setting":{
			"type":"2-motor",
			"wheelSize":"wheel4in",
			"gear":"ratio18_1",
			"gearRatio":"1:1",
			"direction":"fwd",
			"gyroType":"threewire",
			"width":"295",
			"unit":"mm",
			"wheelbase":"40",
			"wheelbaseUnit":"mm",
			"xOffset":"0",
			"xOffsetUnit":"mm",
			"yOffset":"0",
			"yOffsetUnit":"mm",
			"thetaOffset":"180"
		},
		"triportSourcePort":22
	},{
		"port":[],
		"name":"controller_1",
		"customName":false,
		"deviceType":"Controller",
		"deviceClass":"controller",
		"setting":{
			"left":"",
			"leftDir":"false",
			"right":"",
			"rightDir":"false",
			"upDown":"",
			"upDownDir":"false",
			"xB":"",
			"xBDir":"false",
			"drive":"tank",
			"id":"primary"
		},
		"triportSourcePort":22
	},{
		"port":[3,4],
		"name":"fork_motor_group",
		"customName":true,
		"deviceType":"MotorGroup",
		"deviceClass":"motor_group",
		"setting":{
			"fwd":"forward",
			"rev":"reverse",
			"gear":"ratio18_1",
			"motor_a_reversed":"false",
			"motor_b_reversed":"true"
		},
		"triportSourcePort":22
	}],
"slot":0,
"platform":"V5",
"sdkVersion":"20220215.18.00.00",
"appVersion":"",
"fileFormat":"1.0.1",
"icon":"",
"targetBrainGen":"First",
"target":"Physical"
}
```