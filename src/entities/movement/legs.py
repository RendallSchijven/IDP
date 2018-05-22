from entities.movement.limb.leg import Leg


class Legs(object):

    def __init__(self, leg_0_servos, leg_1_servos, leg_2_servos, leg_3_servos):
        """
        Constructor for the legs
        :param leg_0_servos: Array of servo id`s for leg 0
        :param leg_1_servos: Array of servo id`s for leg 1
        :param leg_2_servos: Array of servo id`s for leg 2
        :param leg_3_servos: Array of servo id`s for leg 3
        """

        # Initialise a leg for each corner of the robot
        self.leg_front_left = Leg(leg_0_servos[0], leg_0_servos[1], leg_0_servos[2], 600, 450, 850)
        # self.leg_front_right = Leg(leg_1_servos[0], leg_1_servos[1], leg_1_servos[2], 600, 450, 850)
        # self.leg_rear_left = Leg(leg_2_servos[0], leg_2_servos[1], leg_2_servos[2], 600, 450, 850)
        # self.leg_rear_right = Leg(leg_3_servos[0], leg_3_servos[1], leg_3_servos[2], 600, 450, 850)

        print("Legs setup")

    def move(self, leg_0_moves, leg_1_moves, leg_2_moves, leg_3_moves, delay):
        """
        Function to move the legs together
        :param leg_0_moves: Array of positions for leg 0
        :param leg_1_moves: Array of positions for leg 1
        :param leg_2_moves: Array of positions for leg 2
        :param leg_3_moves: Array of positions for leg 3
        :param delay: Time to wait after executing
        :return: None
        """
        self.leg_front_left.move(leg_0_moves[0], leg_0_moves[1], leg_0_moves[2], delay)
        # self.leg_front_right.move(leg_1_moves[0], leg_1_moves[1], leg_1_moves[2], delay)
        # self.leg_rear_left.move(leg_2_moves[0], leg_2_moves[1], leg_2_moves[2], delay)
        # self.leg_rear_right.move(leg_3_moves[0], leg_3_moves[1], leg_3_moves[2], delay)

    def deploy(self):
        """
        Deploys the legs so they can be used for walking
        :return: None
        """
        
        leg_0_deploy = [0, 0, 0]
        leg_1_deploy = [0, 0, 0]
        leg_2_deploy = [0, 0, 0]
        leg_3_deploy = [0, 0, 0]
        delay = 0.1

        # self.leg_front_left.move(leg_0_deploy[0], leg_0_deploy[1], leg_0_deploy[2], delay)
        # self.leg_front_right.move(leg_1_deploy[0], leg_1_deploy[1], leg_1_deploy[2], delay)
        # self.leg_rear_left.move(leg_2_deploy[0], leg_2_deploy[1], leg_2_deploy[2], delay)
        # self.leg_rear_right.move(leg_3_deploy[0], leg_3_deploy[1], leg_3_deploy[2], delay)

    def retract(self):
        """
        Retracts the legs to they are not in the way
        :return: None
        """
        
        leg_0_retract = [0, 0, 0]
        leg_1_retract = [0, 0, 0]
        leg_2_retract = [0, 0, 0]
        leg_3_retract = [0, 0, 0]
        delay = 0.1
        
        # self.leg_front_left.move(leg_0_retract[0], leg_0_retract[1], leg_0_retract[2], delay)
        # self.leg_front_right.move(leg_1_retract[0], leg_1_retract[1], leg_1_retract[2], delay)
        # self.leg_rear_left.move(leg_2_retract[0], leg_2_retract[1], leg_2_retract[2], delay)
        # self.leg_rear_right.move(leg_3_retract[0], leg_3_retract[1], leg_3_retract[2], delay)
