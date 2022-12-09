from PiicoDev_Unified import sleep_ms
from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Servo import PiicoDev_Servo, PiicoDev_Servo_Driver

pot_claw = PiicoDev_Potentiometer(id=[0,1,0,0],minimum=43, maximum=110)
pot_luff = PiicoDev_Potentiometer(id=[0,0,0,1],minimum=0, maximum=180)
pot_slew = PiicoDev_Potentiometer(id=[1,0,0,0],minimum=10, maximum=170)


controller = PiicoDev_Servo_Driver(address = 64)

claw = PiicoDev_Servo(controller, 4, min_us=600, max_us=2500)
luff = PiicoDev_Servo(controller, 3, min_us=600, max_us=2500)
slew = PiicoDev_Servo(controller, 2, min_us=600, max_us=2500)




while True:
    claw.angle = pot_claw.value
    luff.angle = pot_luff.value
    slew.angle = pot_slew.value
    
    print('{} {} {}'.format(slew.angle,luff.angle,claw.angle))

    sleep_ms(50)

