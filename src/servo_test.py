#!/bin/python

import time

from entities.movement.limb.joints.servo import Servo

servo0 = Servo(13, 500)
servo1 = Servo(31, 500)
servo2 = Servo(63, 500)
servo3 = Servo(14, 500)
servo4 = Servo(18, 500)
servo5 = Servo(61, 500)
servo6 = Servo(53, 500)
servo7 = Servo(1, 500)

# should both move at the same time
while True:
    servo0.move(100, 2)
    servo1.move(100, 2)
    servo2.move(100, 2)
    servo3.move(100, 2)
    servo4.move(100, 2)
    servo5.move(100, 2)
    servo6.move(100, 2)
    servo7.move(100, 2)

    servo0.move(900, 2)
    servo1.move(900, 2)
    servo2.move(900, 2)
    servo3.move(900, 2)
    servo4.move(900, 2)
    servo5.move(900, 2)
    servo6.move(900, 2)
    servo7.move(900, 2)

    servo0.move(500, 2)
    servo1.move(500, 2)
    servo2.move(500, 2)
    servo3.move(500, 2)
    servo4.move(500, 2)
    servo5.move(500, 2)
    servo6.move(500, 2)
    servo7.move(500, 2)

