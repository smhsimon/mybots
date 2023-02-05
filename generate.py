import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("world.sdf")
length = 1
width = 1
height = 1

x = 0
y = 0
z = .5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x - 2, y + 2, z] , size=[length, width, height])
    pyrosim.End()

def Create_Robot():
    pass

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -.5] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5] , size=[length, width, height])
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
    pyrosim.End()

Create_World()
Create_Robot()
Generate_Body()
Generate_Brain()


#old stuff
# a = 0
# b = 0
# c = .5

# for i in range (5):
#     for j in range (5):
#         for k in range(10):
#             pyrosim.Send_Cube(name="Box", pos=[i, j, c + k] , size=[length * ((.9) ** k), width * ((.9) ** k), height * ((.9) ** k)])

# pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
# #pyrosim.Send_Cube(name="Box2", pos=[a, b, c] , size=[length, width, height])
# pyrosim.End()