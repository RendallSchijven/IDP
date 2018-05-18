#!/bin/python

import time  # Import the Time library

import RPi.GPIO as GPIO  # Import the GPIO Library


class DCMotor(object):
    """
    Base class for dc motor
    """

    def __init__(self, pin):

        # Set up the gpio and pins for the use of DC motors
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.pin_motor_forward = 10
        self.pin_motor_backward = 9
        self.pin_pwm = pin
        self.frequency = 2048
        self.stop = 0
        self.current_speed = 0

        GPIO.setup(self.pin_pwm, GPIO.OUT)
        GPIO.setup(self.pin_motor_forward, GPIO.OUT)
        GPIO.setup(self.pin_motor_backward, GPIO.OUT)

        # Create an instance of a pwm motor
        self.pwm_motor = GPIO.PWM(self.pin_pwm, self.frequency)
        self.pwm_motor.start(self.stop)

        print("Setup")

    def stop_motor(self):
        """
        Set the motor speed to 0
        :return: None
        """
        self.pwm_motor.ChangeDutyCycle(self.stop)
        self.current_speed = 0

    def forward(self, duty_cycle, delay):
        """
        Turn the motor forward
        :param duty_cycle: the percentage of available power the motor uses
        :param delay: time to wait after executing
        :return: None
        """
        print("Forwards " + str(duty_cycle))
        GPIO.output(self.pin_motor_forward, GPIO.HIGH)
        GPIO.output(self.pin_motor_backward, GPIO.LOW)
        self.pwm_motor.ChangeDutyCycle(duty_cycle)
        self.current_speed = duty_cycle
        time.sleep(delay)

    def backward(self, duty_cycle, delay):
        """
        Turn the motor backward
        :param duty_cycle: the percentage of available power the motor uses
        :param delay: time to wait after executing
        :return: None
        """
        print("Backwards " + str(duty_cycle))
        GPIO.output(self.pin_motor_forward, GPIO.LOW)
        GPIO.output(self.pin_motor_backward, GPIO.HIGH)
        self.pwm_motor.ChangeDutyCycle(duty_cycle)
        self.current_speed = duty_cycle
        time.sleep(delay)

    def clean_up(self):
        """
        Stop the motors and clean up variables and GPIO
        :return: None
        """
        self.stop_motor()
        self.current_speed = 0
        GPIO.cleanup()


def main():
    motor = DCMotor(18)
    motor.clean_up()


if __name__ == "__main__":
    main()