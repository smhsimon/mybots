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
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [1, 0, 1])
    pyrosim.Send_Cube(name="Backleg", pos=[-0.5, 0, -.5] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [2, 0, 1])
    pyrosim.Send_Cube(name="Frontleg", pos=[0.5, 0, -0.5] , size=[length, width, height])
    pyrosim.End()

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
Create_World()
Create_Robot()