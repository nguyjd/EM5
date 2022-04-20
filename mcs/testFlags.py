## @package mcs.testFlags
# Test flag settings for individual modules
#
# Most modules include standard test flags that can be used to facilitate
# testing and debugging. 
# @author Keith
# @note 03/19/2021: Updated documentation -KS

# test number
testNum = 0

# ---------- System Controllers ----------

# MowBot Control System
MowBotControl_debug = True
MowBotControl_enabled = True
# Drive System Control
DriveSysControl_debug = True
DriveSysControl_enabled = True
DriveSysControl_over = False
# Interrupt System Control
InterruptControl_debug = True
InterruptControl_enabled = True
InterruptControl_over = False

# ---------- Controllers ----------

# Battery Monitor
BatteryMonitor_debug = False
BatteryMonitor_enabled = False
BatteryMonitor_over = False
# Blade control
BladeControl_debug = False
BladeControl_enabled = True
BladeControl_over = False
# Collision Detection - Bumpers
CollisionDetection_debug = False
CollisionDetection_enabled = False
CollisionDetection_over = False
# Drive Control
DriveControl_debug = True
DriveControl_enabled = True
DriveControl_over = False
# Navigation
Navigation_debug = True
Navigation_enabled = True
Navigation_over = False
# Remote Control
RemoteControl_debug = True
RemoteControl_enabled = True
RemoteControl_over = False

# ---------- Firmware ----------

#bumpers
bumper1_debug = False
bumper1_enabled = True
bumper1_over = False
bumper2_debug = False
bumper2_enabled = True
bumper2_over = False
bumper3_debug = False
bumper3_enabled = False
bumper3_over = False
bumper4_debug = False
bumper4_enabled = True
bumper4_over = False
bumper5_debug = False
bumper5_enabled = False
bumper5_over = False
bumper6_debug = False
bumper6_enabled = False
bumper6_over = False
bumper7_debug = False
bumper7_enabled = True
bumper7_over = False
# AMT103 - Encoders
AMT103_over = False
leftEncoder_debug = True
leftEncoder_enabled = True
rightEncoder_debug = False
rightEncoder_enabled = False
# MD30C - Blade Motor Driver
MD30C_debug = False
MD30C_enabled = True
MD30C_over = False
# Relay Control
wheelRelay_debug = False
wheelRelay_enabled = True
RelayControl_over = False
bladeRelay_debug = False
bladeRelay_enabled = False
chargeRelay_debug = False
chargeRelay_enabled = False
# Sabertooth2x60 - Wheel Motors
leftMotor_debug = False
leftMotor_enabled = True
rightMotor_debug = False
rightMotor_enabled = True
Sabertooth2x60_over = False
# Object Detection - LiDar
rpLiDAR_A2M4_R4_debug = True
rpLiDAR_A2M4_R4_enabled = True
rpLiDAR_A2M4_R4_over = False
# GPS 
NEO_M8P_debug = False
NEO_M8P_enabled = True
NEO_M8P_RTK_enabled = True
NEO_M8P_over = False