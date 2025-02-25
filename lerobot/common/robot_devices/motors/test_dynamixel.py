from lerobot.common.robot_devices.motors.dynamixel import DynamixelMotorsBus, DynamixelMotorsBusConfig

motor_name = "gripper"
motor_model = "ax-12a"

config = DynamixelMotorsBusConfig(
    port="/dev/ttyUSB0",
    motors={motor_name + "1": (5, motor_model),
            motor_name + "2": (7, motor_model)},
)
motors_bus = DynamixelMotorsBus(config)
motors_bus.connect()
motors_bus.set_bus_baudrate(115200)
motors_bus.write("Torque_Enable", 1)
motors_bus.write("CW_Angle_Limit", 0)
motors_bus.write("CCW_Angle_Limit", 1023)

position = motors_bus.read("Present_Position")
print("Current position: ", position)

# move from a few motor steps as an example
few_steps = 50
motors_bus.write("Goal_Position", position + few_steps)

# when done, consider disconnecting
motors_bus.disconnect()