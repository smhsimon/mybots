from world import WORLD
from robot import ROBOT
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class SIMULATION:

    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        #targetAngles = c.amplitude_b * numpy.sin(c.frequency_b * numpy.linspace(0, 2 * numpy.pi, c.iterations) + c.phaseOffset_b)
        #numpy.save("data/targetAngles.npy", targetAngles)
        
        for i in range(c.iterations):
            p.stepSimulation()       
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            time.sleep(1 / 60)
            # print(backLegSensorValues)
            # print(frontLegSensorValues)

        # numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
        # numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

    def __del__(self):
        p.disconnect()

