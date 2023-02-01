import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

amplitude_f = numpy.pi / 4
frequency_f = 8
phaseOffset_f = 0

amplitude_b = numpy.pi / 4
frequency_b = 8
phaseOffset_b = 0

#do next block in simulate.py or world.py once
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")

#put into robot.py
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

targetAngles = amplitude_b * numpy.sin(frequency_b * numpy.linspace(0, 2 * numpy.pi, 100) + phaseOffset_b)
numpy.save("data/targetAngles.npy", targetAngles)

for i in range(100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = b"Torso_BackLeg",

        controlMode = p.POSITION_CONTROL,

        targetPosition = amplitude_b * numpy.sin(frequency_b * targetAngles[i] + phaseOffset_b),

        maxForce = 500)

    pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = b"Torso_FrontLeg",

        controlMode = p.POSITION_CONTROL,

        targetPosition = amplitude_f * numpy.sin(frequency_f * targetAngles[i] + phaseOffset_f),

        maxForce = 500)


    time.sleep(1 / 60)
    print(backLegSensorValues)
    print(frontLegSensorValues)

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()


