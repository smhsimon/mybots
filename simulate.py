import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

targetAngles = numpy.linspace(0, 2 * numpy.pi, 100)
numpy.save("data/targetAngles.npy", targetAngles)

exit()
for i in range(100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = b"Torso_BackLeg",

        controlMode = p.POSITION_CONTROL,

        targetPosition = random.random(),

        maxForce = 500)

    pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = b"Torso_FrontLeg",

        controlMode = p.POSITION_CONTROL,

        targetPosition = random.uniform(-numpy.pi / 2, numpy.pi / 2),

        maxForce = 500)


    time.sleep(1 / 60)
    print(backLegSensorValues)
    print(frontLegSensorValues)

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()


