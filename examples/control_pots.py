# Manually control two servos with two PiicoDev Potentiometers and a PiicoDev Servo Driver
from PiicoDev_Unified import sleep_ms
from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

rotary = PiicoDev_Potentiometer(minimum=0, maximum=180)
slide = PiicoDev_Potentiometer(id=[1,0,0,0],minimum=-1, maximum=1)

controller = PiicoDev_Servo_Driver()

positional_servo = PiicoDev_Servo(controller, 1)
continuous_servo = PiicoDev_Servo(controller, 2)

while True:
    positional_servo.angle = rotary.value
    continuous_servo.speed = slide.value
    
    print(positional_servo.angle, continuous_servo.speed)
    sleep_ms(50)
