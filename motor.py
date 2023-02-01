import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
    
    def Prepare_To_Act(self, robot):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.phaseOffset = c.phaseOffset
        self.motorValues = self.amplitude * numpy.sin(self.frequency * numpy.linspace(0, 2 * numpy.pi, c.iterations) + self.phaseOffset)

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(

                bodyIndex = robot,

                jointName = self.jointName,

                controlMode = p.POSITION_CONTROL,

                targetPosition = self.motorValues[t],

                maxForce = 500)